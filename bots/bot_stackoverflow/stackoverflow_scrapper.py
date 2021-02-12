import json
import sys
import logging
import datetime
import time
from selenium.webdriver.common.keys import Keys

with open('config/config.json', 'r') as myfile:
    CONFIG = json.load(myfile)
sys.path.append(CONFIG['REPOSITORY_PATH'])
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='./working_directory/webscraping_logs.log', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())


import common.selenium_functions as selenium_function
import common.captcha_solver as captcha_function


if __name__ == '__main__':
    """The main script for web-scraping"""
    #Some configs
    key_search = "Python"

    try:
        logging.info('Initializing Stackoverflow web-scraping')

        browser = selenium_function.initialize_webdriver()

        logging.info('Going to stackoverflow webpage')
        browser.get('https://stackoverflow.com/')

        logging.info('Waiting webpage load')
        selenium_function.wait_element_appear(10,'//*[@id="search"]/div/input',browser)


        logging.info('Searching for: Python')
        browser.find_element_by_xpath('//*[@id="search"]/div/input').send_keys(key_search)
        browser.find_element_by_xpath('//*[@id="search"]/div/input').send_keys(Keys.ENTER)
        time.sleep(2)


        # A simple example to bypass captcha on stackoverflow
        """try:
            logging.info('checking if captcha has appeared')
            captcha_text = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/h1').text
            if 'Human verification' in captcha_text:
                logging.warning('Captcha has appeared')

                sitekey = '6Lfmm70ZAAAAADvPzM6OhZ8Adi40-78E-aYfc1ZS'
                current_url = browser.current_url

                captcha_response = captcha_function.solve_captcha(current_url,sitekey)

                browser.execute_script(
                    'document.getElementById("g-recaptcha-response").innerHTML = "%s"' % captcha_response)

                logging.info('From here on out, could have another functions to solve captcha :) ')
                time.sleep(222)

        except:
            pass"""


        logging.info('Waiting search load')
        selenium_function.wait_element_appear(10,'//*[@id="nav-questions"]',browser)

        logging.info('Click on public>stackoverflow')

        browser.find_element_by_xpath('//*[@id="nav-questions"]').click()







    except BaseException:
        logging.exception(BaseException)
