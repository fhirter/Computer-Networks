import socket


def start_server(local_ip, local_port):

    buffer_size = 1024

    msg_from_server = "Hello UDP Client"

    bytes_to_send = str.encode(msg_from_server)

    udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    udp_server_socket.bind((local_ip, local_port))

    print("server: up and listening")

    while True:
        print("server: waiting for messages")
        bytes_address_pair = udp_server_socket.recvfrom(buffer_size)

        message = bytes_address_pair[0]

        print("server: message received ", message)

        address = bytes_address_pair[1]

        udp_server_socket.sendto(bytes_to_send, address)
