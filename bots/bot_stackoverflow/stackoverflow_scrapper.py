import json
import sys
import logging
import datetime
with open('config/config.json', 'r') as myfile:
    CONFIG = json.load(myfile)
sys.path.append(CONFIG['REPOSITORY_PATH'])
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='webscraping_logs.log', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())
import common.selenium_functions as selenium_function


if __name__ == '__main__':
    """The main script for web-scraping"""


    try:
        logging.info('asdasdasd')







    except BaseException:
        logging.exception(BaseException)
