import time
import socket

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

    def communicate_with_server(self,sock):
        print("Client started, listening for offer requests...")
        message_from_server = None
        while message_from_server is None:
            print("look for server...")
            # print()
            try:
                # sock.settimeout(1)
                message_from_server = sock.recvfrom(1024)
            except:
                print(" - didn't find - look again")
                continue
        return message_from_server

    def run_client(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.bind(('',UDP_DEST_PORT))
        while True:
            data,addr = self.communicate_with_server(sock)
            print (addr[0])
            break

client = Client()
client.run_client()
