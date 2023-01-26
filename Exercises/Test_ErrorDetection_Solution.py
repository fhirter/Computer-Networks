import unittest
from ErrorDetection_Solution import ErrorDetection


class TestErrerDetection(unittest.TestCase):
    def test_parity_check_valid(self):
        error_detection = ErrorDetection()
        number_with_parity = 0b101101010
        parity = error_detection.is_parity_valid(number_with_parity)

        self.assertEqual(parity, True)

    def test_parity_check_invalid(self):
        error_detection = ErrorDetection()
        number_with_parity = 0b001101010
        parity = error_detection.is_parity_valid(number_with_parity)
        self.assertEqual(parity, False)

    def test_parity_creation(self):
        error_detection = ErrorDetection()
        number = 0b10110101
        expected_parity = 0
        actual_parity = error_detection.get_parity(number)

        self.assertEqual(expected_parity, actual_parity)

if __name__ == '__main__':
    unittest.main()
