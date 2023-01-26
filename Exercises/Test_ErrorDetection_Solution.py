import unittest
from ErrorDetection_Solution import ErrorDetection


class TestErrerDetection(unittest.TestCase):
    def test_parity_check_valid(self):
        error_detection = ErrorDetection()
        number_with_parity = 0b101001011
        parity = error_detection.is_parity_valid(number_with_parity)

        self.assertEqual(parity, True)

    def test_parity_check_invalid(self):
        error_detection = ErrorDetection()
        number_with_parity = 0b001001011
        parity = error_detection.is_parity_valid(number_with_parity)
        self.assertEqual(parity, False)

if __name__ == '__main__':
    unittest.main()
