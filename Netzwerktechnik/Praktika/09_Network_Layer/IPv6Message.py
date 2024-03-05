class IPv6Message:
    def __init__(self, destination_address, payload):
        self.version = 0x6
        self.traffic_class = 0x0  # no specific traffic
        self.flow_label = 0x0  # does not belong to any flow
        self.payload_length = len(payload)
        self.next_header = 59  # no next header
        self.hop_limit = 0xff

        self.source_address = 0x0

        self.destination_address = self.parse_address(destination_address)

        self.payload = payload

    def parse_address(self, address_string):
        if not isinstance(address_string, str):
            return address_string

        # Split the IPv6 address into its hexadecimal parts
        hex_parts = address_string.split(":")

        # Convert the hex parts into a single hexadecimal string
        hex_string = "".join(hex_parts)

        # Convert the hexadecimal string to a decimal number
        return int(hex_string, 16)
