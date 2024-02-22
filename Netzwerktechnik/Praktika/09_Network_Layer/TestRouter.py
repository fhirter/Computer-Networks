import unittest

from Router import Router
from Message import Message


class TestRouter(unittest.TestCase):
    def test_message_forwarding(self):
        '''
        message -> r1 / port 0 -> r1 / port 1 -> r2 / port 0
        '''

        destination = 0b10111
        message = Message(destination, 'Hello World!')

        r1 = Router('R1', 2)
        r2 = Router('R2', 1)

        r1.attach(1, r2, 0)

        r1.update_forwarding_table(destination, 1)

        def callback(msg):
            print(msg.value)
            self.assertEqual(message.value, msg.value)

        r2.ports[0].receive(callback)

        r1.ports[0].send_in(message)


if __name__ == "__main__":
    unittest.main()
