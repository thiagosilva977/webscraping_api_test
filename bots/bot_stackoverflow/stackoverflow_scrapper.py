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
    maximum_pages_search = 1

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
        # I didn't continue because it may take a lot of time, but I filtered the all questions by python term :)
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

        logging.info('Waiting questions page load')
        selenium_function.wait_element_appear(10,'//*[@id="mainbar"]',browser)

        logging.info('Filtering by python')
        browser.find_element_by_xpath('//button[@class= "s-btn s-btn__filled s-btn__sm s-btn__icon ws-nowrap"]').click()
        time.sleep(2)
        browser.find_element_by_xpath('//input[@class= "s-input js-tageditor-replacing"]').click()
        browser.find_element_by_xpath('//input[@class= "s-input js-tageditor-replacing"]').send_keys(key_search)
        browser.find_element_by_xpath('//button[@class= "s-btn s-btn__sm s-btn__primary grid--cell"]').click()
        time.sleep(1)
        browser.find_element_by_xpath('//button[@class= "s-btn s-btn__filled s-btn__sm s-btn__icon ws-nowrap is-selected"]').click()

        time.sleep(3)


        #First of all: Create a page-changer engine
        for i in range(maximum_pages_search):

            #Second Loop: Identify all posts
            #
                #Third Loop: Collect all data from the posts individually
                    # (Maybe scrapy? to be fast)



            browser.find_element_by_xpath('//a[@class="s-pagination--item js-pagination-item"]').click()
            time.sleep(5)







    except BaseException:
        logging.exception(BaseException)
