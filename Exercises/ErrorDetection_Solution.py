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

    def ones_comp_add16(self, num1, num2):
        MOD = 1 << 16
        result = num1 + num2
        return result if result < MOD else (result + 1) % MOD

    def get_checksum(self, array):
        if self.is_length_correct(array):
            array[5] = 0  # set checksum to 0
            result = array[0]
            for i in range(1, len(array)):
                result = self.ones_comp_add16(result, array[i])
            ones_complement = result ^ 0xffff
            return ones_complement

        return False

    def is_length_correct(self, ip_header_array):
        length_field = int(hex(ip_header_array[0])[3:4], 16)
        array_length_16bit_count = length_field*32/16
        return array_length_16bit_count == len(ip_header_array)

    def extract_checksum(self, header_array):
        return header_array[5]

    def split_into_chunk_array(self, string, n):
        return [int(string[i:i + n], 16) for i in range(0, len(string), n)]


if __name__ == '__main__':
    error_detection = ErrorDetection()

    # first hex number: IP Version (4)
    # second hex number: Header length (5x32bit=40hex letters)
    ip_header = "450000340000400040064655c0a829a711f8f827"

    ip_header_array = error_detection.split_into_chunk_array(ip_header, 4)

    given_ip_header_checksum = error_detection.extract_checksum(ip_header_array)
    calculated_ip_header_checksum = error_detection.get_checksum(ip_header_array)

    print("given checksum: " + hex(given_ip_header_checksum))
    print("calculated checksum: " + hex(calculated_ip_header_checksum))
    if given_ip_header_checksum == calculated_ip_header_checksum:
        print("👍 the checksums match!")
    else:
        print("👎 The checksums do not match!")


