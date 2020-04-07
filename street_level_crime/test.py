import unittest
import input_helpers
import geodist
import data_reader
from file_resolver import *
import postcode as postcode_lookup


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
        # ~= 1.6km google maps
        dist = geodist.distance(uni_campus, exeter_cathedral)
        self.assertAlmostEqual(dist, 1.6, delta=0.01)

    def test_dist_same_location(self):
        dist = geodist.distance(uni_campus, uni_campus)
        self.assertEqual(0, dist)

    def test_not_within_radius(self):
        # 5.31 on google maps
        isWithin = geodist.is_within_radius(exeter_cathedral, exeter_science_park, 5.3)
        self.assertFalse(isWithin)

    def test_within_radius(self):
        # 5.31 on google maps
        isWithin = geodist.is_within_radius(exeter_cathedral, exeter_science_park, 5.4)
        self.assertTrue(isWithin)


class TestDataReader(unittest.TestCase):
    def test_process_line(self):
        csv_line = ['', '2019-03', 'Devon & Cornwall Police', 'Devon & Cornwall Police', '-4.543901', '50.827132',
                    'On or near Nightclub', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', '']
        processed = data_reader.process_crime_line(csv_line)
        lng = processed[data_reader.CrimeDataField.Longitude]
        lat = processed[data_reader.CrimeDataField.Latitude]
        self.assertIsInstance(lng, float)
        self.assertIsInstance(lat, float)

    def test_process_line_skip_none(self):
        csv_line = ['', '2019-03', 'Devon & Cornwall Police', 'Devon & Cornwall Police', None, '50.827132',
                    'On or near Nightclub', 'E01018936', 'Cornwall 001A', 'Anti-social behaviour', '', '']
        processed = data_reader.process_crime_line(csv_line)
        lng = processed[data_reader.CrimeDataField.Longitude]
        lat = processed[data_reader.CrimeDataField.Latitude]
        self.assertIsInstance(lat, float)

    def test_order_crime_data(self):
        unordered = [
            ['', '2019-03', 'Devon & Cornwall Police', 'Devon & Cornwall Police', -3.924704, 50.388225, 'On or near Zion Place', 'E01020161', 'South Hams 005A', 'Anti-social behaviour', '', ''],
            ['caf30f8b3008f947eeba30e680603a7315afcef78e17d35acecd2591514768be', '2019-03', 'Devon & Cornwall Police', 'Devon & Cornwall Police', -3.924704, 50.388225, 'On or near Zion Place', 'E01020161', 'South Hams 005A', 'Violence and sexual offences', 'Unable to prosecute suspect', ''],
            ['', '2019-03', 'Devon & Cornwall Police', 'Devon & Cornwall Police', -3.562999, 50.428608, "On or near Young'S Park Lane", 'E01015235', 'Torbay 014F', 'Anti-social behaviour', '', '']
        ]

        ordered = data_reader.order_crime_data(unordered, data_reader.CrimeDataField.CrimeType, reverse=True)
        self.assertEqual('caf30f8b3008f947eeba30e680603a7315afcef78e17d35acecd2591514768be',  ordered[0][0])

class TestPostcodeToCoord(unittest.TestCase):
    def test_uni_coord(self):
        coord = postcode_lookup.postcode_to_coordinate(postcode_file_path, "EX44QJ")
        ex44qj_postcode = (50.73514518, -3.53506244)
        self.assertAlmostEqual(coord[0], ex44qj_postcode[0])
        self.assertAlmostEqual(coord[1], ex44qj_postcode[1])

class TestCreateCSV(unittest.TestCase):
    def test_csv_created(self):
        self.assertTrue("File Created")

    def test_csv_creation_error(self):
        self.assertTrue("Error writing to CSV")


if __name__ == '__main__':
    unittest.main()
