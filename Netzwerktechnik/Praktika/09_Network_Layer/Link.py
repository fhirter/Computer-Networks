from Message import Message


class Link:
    def __init__(self, callback):
        self._callback = callback

    def send(self, message: Message):
        self._callback(message)
