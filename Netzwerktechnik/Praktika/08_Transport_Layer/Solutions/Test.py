import threading
import time
import unittest

from Client import send_message
from Server import start_server


class TestCommunication(unittest.TestCase):
    def test_response(self):
        message = "hello from client"

        ip = "127.0.0.1"
        port = 20001

        print("test: starting server")

        server_thread = threading.Thread(target=start_server, args=(ip, port))
        server_thread.daemon = True
        server_thread.start()
        time.sleep(1)

        print("test: sending message: ", message)
        received_bytes = send_message(ip, port, message)

        received_message = received_bytes[0].decode('UTF-8')

        print("test: received message:", received_message)

        self.assertTrue(isinstance(received_message, str))
