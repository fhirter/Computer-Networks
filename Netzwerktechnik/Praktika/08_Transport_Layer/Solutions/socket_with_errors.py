import socket as socket_lib

AF_INET = socket_lib.AF_INET
SOCK_DGRAM = socket_lib.SOCK_DGRAM


def socket(family, type):
    return UdpSocketWithErrors(family, type)


class UdpSocketWithErrors:
    def __init__(self, family, type):
        self.socket_lib_socket = socket_lib.socket(family=family, type=type)

    def sendto(self, bytes_to_send, server_address_port):
        self.socket_lib_socket.sendto(bytes_to_send, server_address_port)

    def recvfrom(self, buffer_size):
        return self.socket_lib_socket.recvfrom(buffer_size)

    def close(self):
        self.socket_lib_socket.close()
