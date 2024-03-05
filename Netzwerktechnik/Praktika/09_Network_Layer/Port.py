class Port:
    def __init__(self, port_id):
        self._callback = None
        self.port_id = port_id
        self.connected_port = None

    def send_in(self, message):
        self._callback(message)

    def send_out(self, message):
        self.connected_port.send_in(message)

    def receive(self, callback):
        self._callback = callback

    def connect(self, other_port):
        self.connected_port = other_port
        other_port.connected_port = self

    def disconnect(self):
        if self.connected_port:
            self.connected_port.connected_port = None
            self.connected_port = None
