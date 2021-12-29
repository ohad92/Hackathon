import time
import socket
from scapy.all import *
import getch
import message_utils as msg

# dev_server_IP = get_if_addr('eth1')
# test_server_IP = get_if_addr('eth2')
UDP_DEST_PORT = 13117
SERVER_PORT = 2063
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
            sock.bind(('',UDP_DEST_PORT))
            message_from_server = None
            # search for server
            while True:
                # if message_from_server == MAGIC_COOKIE:
                #     break
                time.sleep(0.5)
                data, addr = sock.recvfrom(1024)
                server_ip = addr[0]
                port = data[2]
                print(msg.client_attempt_connect(server_ip))
                try:
                    # sock.settimeout(1)
                    data = struct.unpack("IbH",data)
                    message_from_server = data
                    if server_ip == "172.1.0.63":
                        break
                except Exception as e:
                    print(e)
                    continue

            #connecting to server
            print("before TCP client connect")
            try:
                print("trying to connect TCP")
                self.tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.tcp_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
                self.tcp_sock.connect((server_ip,port))
                self.tcp_sock.sendall((self.name + "\n").encode('utf-8'))
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
