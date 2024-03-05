import unittest

from Client import Client
from Router import Router
from IPv6Packet import IPv6Packet


class TestRouter(unittest.TestCase):
    def test_message_forwarding(self):
        '''
        message -> r1 / port 0 -> r1 / port 1 -> r2 / port 0 -> client / port 0
        '''

        destination_address = "2345:0425:2CA1:0000:0000:0567:5673:23b5"

        message = IPv6Packet(destination_address, 'Hello World!')

        def callback(msg):
            print(f"Message received: {message.payload}")
            self.assertEqual(message.payload, msg.payload)

        r1 = Router('R1', 2)
        r2 = Router('R2', 2)
        client = Client('C1', callback)

        r1.attach(1, r2, 0)
        r2.attach(1, client, 0)

        r1.update_forwarding_table(destination_address, 1)
        r2.update_forwarding_table(destination_address, 1)

        r1.ports[0].send_in(message)


if __name__ == "__main__":
    unittest.main()
