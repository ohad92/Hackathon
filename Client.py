import time
import socket
from scapy.all import *
# import message_utils as msg

# dev_server_IP = get_if_addr('eth1')
# test_server_IP = get_if_addr('eth2')
UDP_DEST_PORT = 13117
SERVER_PORT = 2063
MAGIC_COOKIE = 0xabcddcba
MESSAGE_TYPE = 0x2
IP_ADDRESS = "192.168.1.25"
SERVER_IP = IP_ADDRESS

class Client:
    def __init__(self):
        self.name = "einat_sarof"



    def run(self):
        while True:
            print("back")
            sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            sock.bind(('',UDP_DEST_PORT))
            message_from_server = None
            # search for server
            while message_from_server is None:
                if message_from_server == MAGIC_COOKIE:
                    break
                data,addr = sock.recvfrom(1024)
                try:
                    # sock.settimeout(1)
                    data = struct.unpack("Ibh",data)
                    # message_from_server = data
                    # print(message_from_server)
                    # break
                    print (data)
                    # if data[0] == MAGIC_COOKIE:
                    #     message_from_server = MAGIC_COOKIE

                except:
                    print(" - didn't find - look again")
                    continue
            # sock.close()

            #connecting to server
            # try:
            #     tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            #     tcp.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            #     tcp.connect(adrr[0],data[2])
            #     tcp.send(str.encode(self.name + "\n"))
            # except:
            #     print ("connection failed tcp")

            # if tcp is None:
            #     continue

client = Client()
client.run()
