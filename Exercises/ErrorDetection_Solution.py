class ErrorDetection:
    def is_parity_valid(self, number):
        # extract payload and parity
        binary_string = bin(number)
        parity_bit = binary_string[-1]
        binary_string = binary_string[2:-2]

        # counte occurences of '1'
        one_count = binary_string.count('1')

        # check if occurences count is odd or even and compare to parity bit
        is_valid = (one_count % 2) == int(parity_bit)
        return is_valid

    def get_parity(self, number):
        binary_string = bin(number)
        one_count = binary_string.count('1')
        one_count += 1 # increment to get even parity
        parity = (one_count % 2)
        return parity
