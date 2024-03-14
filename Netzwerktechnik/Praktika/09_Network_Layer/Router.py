from Port import Port
from IPv6Packet import IPv6Packet

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

    def __forward(self, message: IPv6Packet):
        destination = message.destination_address
        if destination not in self.forwarding_table:
            print(f"No forwarding entry for {destination}")
            return

        port_id = self.forwarding_table[destination]

        if port_id > len(self.ports):
            print(f"Port {port_id} not present!")
            return

        port = self.ports[port_id]
        print(f"Forwarded Packet to {destination} at Router {self.router_id}")
        port.send_out(message)


    def attach(self, port_id, other_router, other_port_id):
        self.ports[port_id].connect(other_router.ports[other_port_id])
