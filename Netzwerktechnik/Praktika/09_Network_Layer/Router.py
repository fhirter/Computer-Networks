from Port import Port
import Message


class Router:
    def __init__(self, router_id, num_ports):
        self.router_id = router_id
        self.forwarding_table = {}  # Format: {destination_address: port_id}
        self.ports = []
        for i in range(num_ports):
            port = Port(i)

            port.receive(self.__forward)
            self.ports.append(port)

    def update_forwarding_table(self, destination, port_id):
        self.forwarding_table[destination] = port_id

    def __forward(self, message: Message):
        destination = message.destination
        if destination in self.forwarding_table:
            port_id = self.forwarding_table[destination]
            port = self.ports[port_id]
            port.send_out(message)
        else:
            print(f"No forwarding entry for {destination}")

    def attach(self, port_id, other_router, other_port_id):
        self.ports[port_id].connect(other_router.ports[other_port_id])
