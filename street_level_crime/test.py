import unittest
import input_helpers
import geodist

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

uni_campus = (50.736544, -3.534948)
exeter_cathedral = (50.722548, -3.529915)
exeter_science_park = (50.731379, -3.455758)


class GeodistTest(unittest.TestCase):
    def test_dist_uni_to_cathedral(self):
        #~= 1.6km google maps
        dist = geodist.distance(uni_campus, exeter_cathedral)
        self.assertAlmostEqual(dist, 1.6, delta=0.01)

    def test_dist_same_location(self):
        dist = geodist.distance(uni_campus, uni_campus)
        self.assertEqual(0, dist)

    def test_not_within_radius(self):
        #5.31 on google maps
        isWithin = geodist.is_within_radius(exeter_cathedral, exeter_science_park, 5.3)
        self.assertFalse(isWithin)
    
    def test_within_radius(self):
        #5.31 on google maps
        isWithin = geodist.is_within_radius(exeter_cathedral, exeter_science_park, 5.4)
        self.assertTrue(isWithin)


if __name__ == '__main__':
    unittest.main()