import threading
import unittest
from unittest import TestCase

from Client import send_message
from Server import start_server


class TestCommunication(unittest.TestCase):
    def test_response(self):
        expected_message = "Hello UDP Client"

        message = "hello from client"

        ip = "127.0.0.1"
        port = 20001

        print("test: starting server")

        server_thread = threading.Thread(target=start_server, args=(ip, port))
        server_thread.daemon = True
        server_thread.start()
        time.sleep(1)

        print("test: sending message")
        received_bytes = send_message(ip, port, message)

        received_message = received_bytes[0].decode('UTF-8')

        print("received message", received_message)

        self.assertEqual(received_message, expected_message)

        # todo: stop server and join thread to avoid tests running indefinitely
