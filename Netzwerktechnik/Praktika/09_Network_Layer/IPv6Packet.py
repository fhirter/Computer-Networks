from helpers import parse_address


class IPv6Packet:
    def __init__(self, destination_address, payload):
        self.version = 0x6
        self.traffic_class = 0x0  # no specific traffic
        self.flow_label = 0x0  # does not belong to any flow
        self.payload_length = len(payload)
        self.next_header = 59  # no next header
        self.hop_limit = 0xff

        self.source_address = 0x0

        self.destination_address = parse_address(destination_address)

        self.payload = payload
