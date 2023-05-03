import re

# Define the encoding table for 4b5b encoding
encoding_table = {
    "0000": "11110",
    "0001": "01001",
    "0010": "10100",
    "0011": "10101",
    "0100": "01010",
    "0101": "01011",
    "0110": "01110",
    "0111": "01111",
    "1000": "10010",
    "1001": "10011",
    "1010": "10110",
    "1011": "10111",
    "1100": "11010",
    "1101": "11011",
    "1110": "11100",
    "1111": "11101",
}

def convert_to_binary(input_string):
    # Convert the input string to a binary sequence using ASCII encoding
    binary_str = ''.join(format(ord(c), '08b') for c in input_string)
    return binary_str


def encode_4b5b(binary_string):
    # Split the binary sequence into 4-bit blocks
    binary_blocks = re.findall('.{4}', binary_string)
    # Encode each block using 4b5b encoding
    encoded_blocks = [encoding_table[block] for block in binary_blocks]
    # Combine the encoded blocks into a single string
    encoded_str = ''.join(encoded_blocks)
    return encoded_str

def count_consecutive_bits(binary_string):
    # Count the number of consecutive 0s and 1s in the binary sequence
    consecutive_zeros = [len(match) for match in re.findall('0+', binary_string)]
    consecutive_ones = [len(match) for match in re.findall('1+', binary_string)]
    return consecutive_zeros, consecutive_ones

def calculate_mean(binary_string):
    ones_count = binary_string.count('1')
    length = len(binary_string)
    return ones_count/length


# Example usage
input_string = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna "
binary_string = convert_to_binary(input_string)
print("Binary sequence:", binary_string)
encoded_str = encode_4b5b(binary_string)
print("Encoded sequence:", encoded_str)
encoded_zeros, encoded_ones = count_consecutive_bits(encoded_str)
unencoded_zeros, unencoded_ones = count_consecutive_bits(binary_string)

encoded_mean = calculate_mean(encoded_str)
unencoded_mean = calculate_mean(binary_string)

print("Max number of consecutive 0s and 1s")
print("unencoded sequence:", max(unencoded_zeros), max(unencoded_ones))
print("encoded sequence:", max(encoded_zeros),  max(encoded_ones))

print("Mean value")
print("unencoded sequence", encoded_mean)
print("encoded sequence", unencoded_mean)
