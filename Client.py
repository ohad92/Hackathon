import time
import socket
from scapy.all import *
import getch
import message_utils as msg

# dev_server_IP = get_if_addr('eth1')
# test_server_IP = get_if_addr('eth2')
UDP_DEST_PORT = 13177
# SERVER_PORT = 2063
MAGIC_COOKIE = 0xabcddcba
MESSAGE_TYPE = 0x2
# IP_ADDRESS = "192.168.1.25"
# SERVER_IP = dev_server_IP

class Client:
    def __init__(self):
        self.name = "einat_sarof"
        self.tcp_sock = None

    def run(self):
        while True:
            print("back")
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
            # sock.bind(('',UDP_DEST_PORT))
            message_from_server = None
            print("before while")
            # search for server
            while True:
                sock.bind(('',UDP_DEST_PORT))
                packet, adrr= sock.recvfrom(1024)
                try:
                    Message = struct.unpack("Ibh",packet)
                    print(Message)
                    if (int(Message[0]) == MAGIC_COOKIE and int(Message[1] == MESSAGE_TYPE)): ##making sure we only accept packets with the correct format
                        #int(Message[2] == 2113) is for test purpose only the port of OUR server
                        port=Message[2]
                        print(port)
                        # self.tcp_ip_address=adrr[0] #setting the ip address that will be used for the tcp client
                        # print(self.tcp_ip_addre/ss)
                        print("Concting to server on port ", port)
                        # return port
                        break
                except Exception as e:
                    time.sleep(1)


                # print("inside while - start")
                # # if message_from_server == MAGIC_COOKIE:
                # #     break
                # time.sleep(0.5)
                # try:
                #     data, addr = sock.recvfrom(2048)
                # except Exception as e:
                #     print(e)
                # print(f"recieved message {data}")
                # server_ip = addr[0]
                # magicookie = int(data[0])
                # msg_type = int(data[1])
                # port = int(data[2])
                # print(magicookie)
                # print(msg_type)
                # print(port)
                # print(msg.client_attempt_connect(server_ip))
                # try:
                #     # sock.settimeout(1)
                #     data = struct.unpack("Ibh",data)
                #     message_from_server = data
                #     print("GOT HERE ?")
                #     print(server_ip)
                #     if magicookie == MAGIC_COOKIE:
                #         break
                # except Exception as e:
                #     print(e)
                #     continue

            #connecting to server
        #     try:
        #         clientSocket = socket(AF_INET, SOCK_STREAM)
        #         break
        #     except :
        #         print("error creating socket. trying again")
        #         counter+=1
        #         if(counter==self.counter_limit):
        #             print("starting a new game")
        # connected = False
        # i = -1 ###todo look here =-1
        # while not connected:
        #     try:
        #         clientSocket.connect(server_address) #connecting to


            print("before TCP client connect")
            try:
                print("trying to connect TCP")
                tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                print("socket1")
                tcp_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
                print("socket2")
                print(adrr[0])
                tcp_sock.connect(("172.1.0.63",port))
                print("connecting?")
                tcp_sock.sendall((self.name).encode('utf-8'))
                print("TCP CONNECTED")
                break
            except Exception as e:
                print(e)

            if self.tcp_sock is None:
                continue
        self.play()
    
    def play(self):
        # # send to server name and IP
        # msg_name = self.name
        # self.tcp_sock.send()
        print("Client TRYING TO PLAYYY")
        question_from_server = str(self.tcp_sock.recv(1024), 'utf-8')
        print(question_from_server)
        print("Type an answer to the question: ")
        user_input_ans = getch.getch()
        print(user_input_ans)
        # send answer to server
        self.tcp_sock.send(str.encode(self.name + "\n"))

client = Client()
client.run()
