import socket
from scapy.all import *
import message_utils as msg

dev_server_IP = get_if_addr('eth1')
test_server_IP = get_if_addr('eth2')
# print(f"dev: {dev_server_IP}, test: {test_server_IP}")
UDP_DEST_PORT = 13117
SERVER_PORT = 2063
MAGIC_COOKIE = 0xabcddcba
MESSAGE_TYPE = 0x2
IP_ADDRESS = "132.72.200.182"
SERVER_IP = dev_server_IP


class Server:
    def __init__(self):
        self.alive_status = False
        self.clients_num = 0
        self.player1 = None
        self.player2 = None
        self.question = None
        self.correct_ans = None


    def start(self):
        self.alive_status = True
        self.start_udp()
        self.connect_clients()
        
        
    def start_udp(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # sock.bind((SERVER_IP, UDP_DEST_PORT))
        packet_msg = struct.pack("Ibh", MAGIC_COOKIE, MESSAGE_TYPE, SERVER_PORT) #I-int (4 bytes), B-byte (1 bytes), H-short (2 bytes)
        print(msg.server_started(SERVER_IP))
        while True:
            sock.sendto(packet_msg, ("<broadcast>", UDP_DEST_PORT))
            # time.sleep(1)
            print("send again")
            self.connect_clients()
            if(self.clients_num >=2):
                break
        return


    def connect_clients(self):
        print("start tcp")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((SERVER_IP, UDP_DEST_PORT))
        sock.listen(100)
        # First player
        while True:
            try:
                print("looking for tcp client 1 connect !")
                client_ip, client_addr = sock.accept()
                print(client_ip)
                print(client_addr)
                self.player1 = (client_ip, client_addr, client_ip.recv(1024).decode)
                self.clients_num += 1
                break
            except:
                print("try again connecting to tcp")
                continue
        # Second player
        while True:
            try:
                print("looking for tcp client 2 connect !")
                client_ip, client_addr = sock.accept()
                print(client_ip)
                print(client_addr)
                self.player2 = (client_ip, client_addr, client_ip.recv(1024).decode)
                self.clients_num += 1
                break
            except:
                print("try again connecting to tcp")
                continue    
        
        if self.player1!=None and self.player2!=None:
            self.game()
    # def connect_clients(self):
    #     while self.clients_num < 2:
    #         print("looking for clients to play :)")
    #         # create TCP connection - with start_tcp
    #         t1 = threading.Thread(target=self.start_tcp, args=())
    #         t2 = threading.Thread(target=self.start_tcp, args=())
    #         t1.start()
    #         t2.start()
    #         t1.join()
    #         t2.join()

        # GAME
    
        print("connect")

    def game(self):
        questions_bank= {"1+1":2, "1+2":3, "2+2":4, "2+3":5}
        # get a question and answer save it
        self.question = random.choice(list(questions_bank))
        game_msg = msg.start_game_message(self.player1[2], self.player2[2], self.question)
        print(game_msg)
        # send to both players

        try:
            self.player1[0].send(str.encode(game_msg))
        except:
            print("connection lost ... ")
            return
        try:
            self.player2[0].send(str.encode(game_msg))
        except:
            print("connection lost ... ")
            return
        time.sleep(10) #wait 10 seconds before starting
        # wait for a player to answer
        start_time = time.time()
        # while time.time() < start_time + 10:
        #     try:
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
