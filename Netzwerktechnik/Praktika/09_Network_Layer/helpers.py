def parse_address(address_string):
    if not isinstance(address_string, str):
        return address_string

    # Split the IPv6 address into its hexadecimal parts
    hex_parts = address_string.split(":")

    # Convert the hex parts into a single hexadecimal string
    hex_string = "".join(hex_parts)

    # Convert the hexadecimal string to a decimal number
    return int(hex_string, 16)