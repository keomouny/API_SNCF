import logging
import os

# path_file_current = f'{os.getcwd()}/manipulation_api_csv' if '/manipulation_api_csv' not in os.getcwd() else os.getcwd()

logging.basicConfig(filename="logs/log.log", filemode="a",
                    format="%(asctime)s - %(levelname)-8s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S", level=logging.DEBUG)

logger = logging.getLogger(__name__)
