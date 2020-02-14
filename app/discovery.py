from time import sleep
from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST, gethostbyname, gethostname


class Discovery:

    def __init__(self, port: int):

        self.port = port

        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.bind(('', 0))
        self.socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

        local_ip_addr = gethostbyname(gethostname())
        flag = "SignCoach"
        self.data = flag+local_ip_addr

    def publish_packet(self):
        self.socket.sendto(bytes(self.data), ('<broadcast>', self.port))