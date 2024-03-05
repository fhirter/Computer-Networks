from IPv6Packet import IPv6Packet


class Link:
    def __init__(self, callback):
        self._callback = callback

    def send(self, message: IPv6Packet):
        self._callback(message)
