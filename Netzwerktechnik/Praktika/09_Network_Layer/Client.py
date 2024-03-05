from Port import Port
import Message


class Client:
    def __init__(self, client_id, callback):
        self.id = client_id

        self.ports = []

        port = Port(0)
        port.receive(callback)
        self.ports.append(port)

    def attach(self, port_id, other_router, other_port_id):
        self.ports[port_id].connect(other_router.ports[other_port_id])



