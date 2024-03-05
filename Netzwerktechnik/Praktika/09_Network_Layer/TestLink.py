import unittest

from Link import Link
from IPv6Message import IPv6Message


class TestLink(unittest.TestCase):
    def test_message_forwarding(self):
        destination = 0b10111
        message = IPv6Message(destination, 'Hello World!')

        def callback(msg):
            self.assertEqual(message.value, msg.value)

        link = Link(callback)
        link.send(message)