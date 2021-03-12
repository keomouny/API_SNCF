import unittest
import os
from index_bis import get_data_from_json, get_header_columns, list_gares, get_all_areas


class TestMethodsApi(unittest.TestCase):

    def test_file_json_exists(self):
        self.assertTrue(os.path.isfile('stop_areas.json'))

    def test_file_csv_exists(self):
        self.assertTrue(os.path.exists('stop_areas.csv'))

    def test_get_data_from_json(self):
        self.assertIs(type(get_data_from_json()), dict)

    def test_get_header_columns(self):
        self.assertIs(type(get_header_columns(list_gares)), list)

    def test_get_all_areas(self):
        self.assertIs(type(get_all_areas(list_gares)), list)
        self.assertEqual(len(get_all_areas(list_gares)), 25)


if __name__ == '__main__':
    unittest.main(verbosity=2)
