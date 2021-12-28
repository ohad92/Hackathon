import socket
from scapy.all import *
import message_utils as msg

dev_server_IP = get_if_addr('eth1')
test_server_IP = get_if_addr('eth2')
UDP_DEST_PORT = 13117
SERVER_PORT = 2063
MAGIC_COOKIE = 0xabcddcba
MESSAGE_TYPE = 0x2
IP_ADDRESS = "127.0.0.1"
SERVER_IP = IP_ADDRESS


class Server:
    def __init__(self):
        self.alive_status = False

    def start(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind((SERVER_IP, UDP_DEST_PORT))
        self.alive_status = True
        packet_msg = struct.pack("Ibh", MAGIC_COOKIE, MESSAGE_TYPE, SERVER_PORT) #I-int (4 bytes), B-byte (1 bytes), H-short (2 bytes)
        msg.server_started(SERVER_IP)

        while True:
            sock.sendto(packet_msg, (SERVER_IP, UDP_DEST_PORT))
            time.sleep(1)

    def connect_clients(self):
        print("connect")

        
if __name__ == '__main__':
    server = Server()
    server.start()
