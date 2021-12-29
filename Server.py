import socket
from scapy.all import *
import message_utils as msg

dev_server_IP = get_if_addr('eth1')
test_server_IP = get_if_addr('eth2')
# print(f"dev: {dev_server_IP}, test: {test_server_IP}")
UDP_DEST_PORT = 13177
SERVER_PORT = 2063
MAGIC_COOKIE = 0xabcddcba
MESSAGE_TYPE = 0x2
SERVER_IP = dev_server_IP


class Server:
    def __init__(self):
        self.alive_status = False
        self.clients_num = 0
        self.players= []
        self.question = None
        self.correct_ans = None
        self.sockets = []


    def start(self):
        self.alive_status = True
        udpthread = threading.Thread(target=self.start_udp)
        udpthread.start()
        t1 = threading.Thread(target=self.start_Tcp_server)
        # t2 = threading.Thread(target=self.connect_clients)
        t1.start()
        # t2.start()
        udpthread.join()
        t1.join()
        # t2.join()

    def start_Tcp_server(self):
        """
        multi threaded function that start the Tcp Server and make a thread for each client.
        """
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.setblocking(True)
        serverSocket.bind(('', SERVER_PORT))
        serverSocket.listen(2)
        Threads = []
        serverSocket.settimeout(10)
        # start_time = time.time() + 10

        try:
            while self.clients_num < 2:
                connectionSocket, addr = serverSocket.accept()
                Threads.append(Thread(target=self.game, args=(connectionSocket,)))
        except timeout:
            print("Not enogh players to play")

        print("Game is ready")
        for x in Threads:
            x.start()

        # wait for all the threads to finish
        for x in Threads:
            x.join()
        
        
    def start_udp(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # sock.bind((SERVER_IP, UDP_DEST_PORT))
        packet_msg = struct.pack("Ibh", MAGIC_COOKIE, MESSAGE_TYPE, SERVER_PORT) #I-int (4 bytes), B-byte (1 bytes), H-short (2 bytes)
        print(MAGIC_COOKIE,MESSAGE_TYPE,SERVER_PORT)
        while True:
            sock.sendto(packet_msg, ("<broadcast>", UDP_DEST_PORT))
            time.sleep(1)
            print(msg.server_started(SERVER_IP))
            if(self.clients_num >=2):
                break
        return

    def connect_clients(self):
        print("start tcp")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((SERVER_IP, SERVER_PORT))
        sock.listen(1)
        sock.settimeout(1)
        # self.sockets.append(sock)
        # add players
        while True:
            try:
                print(len(self.sockets))
                print("looking for tcp client connection !")
                client_ip, client_addr = sock.accept()
                print(client_ip)
                print(client_addr)
                self.players.append((client_ip, client_addr, client_ip.recv(1024).decode))
                self.clients_num += 1
                break
            except:
                print("try again connecting to tcp")
                continue
        
        # GAME
    def get_question():
        questions_bank= {"1+1":2, "1+2":3, "2+2":4, "2+3":5}
        # get a question and answer save it
        self.question = random.choice(list(questions_bank))

    def game(self):
        game_msg = msg.start_game_message(self.players[0][2], self.players[1][2], self.question)
        print(game_msg)
        # send to both players
        try:
            self.players[0][0].send(str.encode(game_msg))
        except:
            print("connection lost ... ")
            return
        try:
            self.players[0][0].send(str.encode(game_msg))
        except:
            print("connection lost ... ")
            return
        time.sleep(10) #wait 10 seconds before starting
        # wait for a player to answer
        start_time = time.time()
        client_answer = []
        while time.time() < start_time + 10:
            try:
                client_answer = []
                for i in range(len(self.players)):
                    print("hello")
            except:
                print("BUMMER")
        if len(client_answer) > 0:
            print("cool")
        else:
            print("not cool")
            # draw
    # for i in len(client_answer):

        
    def get_answer():
        return int(player[0].recv(1024)), time.time()
                        
                        
        #         client_answer
        # check answer
        # correct -> player wins
        # wrong -> other player wins
        # no answer 10 secondds -> draw
        # close session
        # start again

if __name__ == '__main__':
    server = Server()
    server.start()
