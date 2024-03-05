from IPv6Message import IPv6Message


class Link:
    def __init__(self, callback):
        self._callback = callback

    def send(self, message: IPv6Message):
        self._callback(message)
