import requests
import json
import csv
import os
from pprint import pprint
from dotenv import load_dotenv
from setup_logger import logger


class ApiSncf:
    # constructor
    def __init__(self):
        logger.info('Instanciation of ApiSncf class')
        load_dotenv()
        self.url_api = 'https://api.sncf.com/v1/coverage/sncf/stop_areas?count=1000'
        self.token_auth = os.environ.get('TOKEN_AUTH')
        self.filename_export = 'stop_areas'
        self.request_api_sncf = None
        self.list_gares = []

    # check if object from stap areas contain keys below
    def get_header_columns(self):
        logger.info('check header from columns for create csv file')
        for element in self.list_gares:
            if all(el in element for el in ('id', 'coord', 'name', 'admin_region_id', 'admin_region_name', 'admin_region_zip_code', 'admin_region_insee')):
                return [i for i in element.keys()]

    # create csv file with data list of stop areas
    def create_csv(self):
        try:
            list_header_columns = self.get_header_columns()
            with open(f'files/csv/{self.filename_export}.csv', 'w') as csvfile:
                writer = csv.DictWriter(
                    csvfile, fieldnames=list_header_columns)
                writer.writeheader()
                for data in self.list_gares:
                    writer.writerow(data)
        except IOError:
            logger.error("I/O error")
            print('create csv failed')

    # read data from url address and get it to json file
    def read_url_json(self, url_test):
        request_api = requests.get(url_test, auth=(self.token_auth, ''))
        if request_api.status_code == 200:
            with open(f'files/json/{self.filename_export}.json', 'w') as outfile:
                json.dump(request_api.json(), outfile, indent=4)
        else:
            print('request Not found')

    # get data from json file and keep it in property named request_api_sncf
    def get_data_from_json(self):
        with open(f'files/json/{self.filename_export}.json') as json_file:
            self.request_api_sncf = json.load(json_file)

    # get data from property request_api_sncf and keep it in list_gares property
    def get_all_areas(self, areas):
        for loop_area in areas:
            if type(loop_area) == dict:
                dict_gare = {}
                if 'id' in loop_area.keys():
                    dict_gare['id'] = loop_area['id']
                else:
                    print('missing key id')

                if 'coord' in loop_area.keys():
                    dict_gare['coord'] = loop_area['coord']
                else:
                    print('missing key coord')

                if 'name' in loop_area.keys():
                    dict_gare['name'] = loop_area['name']
                else:
                    print('missing key name')

                if 'administrative_regions' in loop_area.keys():
                    ad_region_data = loop_area['administrative_regions'][0]
                    dict_gare['admin_region_id'] = ad_region_data['id']
                    dict_gare['admin_region_name'] = ad_region_data['name']
                    dict_gare['admin_region_zip_code'] = ad_region_data['zip_code']
                    dict_gare['admin_region_insee'] = ad_region_data['insee']
                else:
                    print('missing key administrative region')

                self.list_gares.append(dict_gare)
                dict_gare = {}
            else:
                print(f'Unexpected format {type(loop_area)}')

    # start application
    def app_start(self):
        self.read_url_json(self.url_api)
        self.get_data_from_json()
        self.get_all_areas(self.request_api_sncf['stop_areas'])
        self.create_csv()
