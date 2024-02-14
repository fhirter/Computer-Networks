import socket


def start_server(local_ip, local_port):

    buffer_size = 1024

    f = open("answer_short.txt", "r")
    lines = f.readlines()
    response = "".join(lines)
    f.close()

    bytes_to_send = str.encode(response)

    udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    udp_server_socket.bind((local_ip, local_port))

    print("server: up and listening")

    while True:
        print("server: waiting for messages")
        [message, address] = udp_server_socket.recvfrom(buffer_size)

        print("server: message received ", message)

        udp_server_socket.sendto(bytes_to_send, address)
