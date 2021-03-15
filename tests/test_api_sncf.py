import unittest
import os
from api_sncf import api_sncf
import requests


class ApiSncfTestCase(unittest.TestCase):

    def setUp(self):
        self.ApiSncf = api_sncf.SncfApi()

    def test_file_json_exists(self):
        self.assertTrue(os.path.isfile('stop_areas.json'))

    def test_file_csv_exists(self):
        self.assertTrue(os.path.exists('stop_areas.csv'))

    def test_get_data_from_json(self):
        self.assertEqual(self.ApiSncf.request_api_sncf, None)

    def test_get_header_columns(self):
        self.assertIs(type(self.ApiSncf.list_header_columns), list)

    def test_get_all_areas(self):
        self.assertIs(type(self.ApiSncf.list_gares), list)
        self.assertEqual(
            len(self.ApiSncf.get_all_areas(self.ApiSncf.list_gares)), 25)

    def test_status_code(self):
        res = requests.get(self.ApiSncf.url_api,
                           auth=(self.ApiSncf.token_auth, ''))
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
