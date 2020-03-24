import unittest
import input_helpers

class UIHelpersTests(unittest.TestCase):
    def test_valid_postcode_no_spaces(self):
        isValid = input_helpers.validate_postcode("EX44QJ")
        self.assertTrue(isValid)

    def test_valid_postcode_spaces(self):
        isValid = input_helpers.validate_postcode("EX4 4QJ")
        self.assertTrue(isValid)

    def test_valid_postcode_cases_insenstive(self):
        isValid = input_helpers.validate_postcode("eX44qJ")
        self.assertTrue(isValid)

    def test_invalid_postcode(self):
        isValid = input_helpers.validate_postcode("APPLE")
        self.assertFalse(isValid)

if __name__ == '__main__':
    unittest.main()