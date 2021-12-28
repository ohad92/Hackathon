import time
import socket

# dev_server_IP = get_if_addr('eth1')
# test_server_IP = get_if_addr('eth2')
UDP_DEST_PORT = 13117
SERVER_PORT = 2063
MAGIC_COOKIE = 0xabcddcba
MESSAGE_TYPE = 0x2
IP_ADDRESS = "127.0.0.1"
SERVER_IP = IP_ADDRESS

class Client:
    def __init__(self):
        self.name = "einat_sarof"

    def communicate_with_server():
        print("Client started, listening for offer requests...")
        UDP_Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        UDP_Socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
        UDP_Socket.bind(('',UDP_DEST_PORT))
        message_from_server = None
        while message_from_server is None:
            try:
                UDP_Socket.settimeout(1)
                message_from_server = UDP_Socket.recvfrom(1024)
            except:
                continue
        return message_from_server

    def run_client():
        while True:
            data,addr = communicate_with_server()
            print (addr[0])
            break

