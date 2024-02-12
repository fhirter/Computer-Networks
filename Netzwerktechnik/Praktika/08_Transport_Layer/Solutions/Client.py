import socket


def send_message(ip, port, message):
    bytes_to_send = str.encode(message)

    server_address_port = (ip, port)

    buffer_size = 1024

    udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    udp_client_socket.sendto(bytes_to_send, server_address_port)

    msg_from_server = udp_client_socket.recvfrom(buffer_size)

    udp_client_socket.close()

    return msg_from_server

