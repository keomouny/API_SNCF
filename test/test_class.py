import unittest
import os
from manipulation_api_csv.api_sncf import ApiSncf
import requests


class TestMethods(unittest.TestCase):

    def test_file_json_exists(self):
        self.assertTrue(os.path.isfile('stop_areas.json'))

    def test_file_csv_exists(self):
        self.assertTrue(os.path.exists('stop_areas.csv'))

    def test_get_data_from_json(self):
        api_sncf = ApiSncf()
        self.assertEqual(api_sncf.request_api_sncf, None)

    def test_get_header_columns(self):
        api_sncf = ApiSncf()
        self.assertIs(type(api_sncf.list_header_columns), list)

    def test_get_all_areas(self):
        api_sncf = ApiSncf()
        self.assertIs(type(api_sncf.list_gares), list)
        self.assertEqual(len(api_sncf.get_all_areas(api_sncf.list_gares)), 25)

    def test_status_code(self):
        api_sncf = ApiSncf()
        res = requests.get(api_sncf.url_api, auth=(api_sncf.token_auth, ''))
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
