import os
import time
import json
import logging
import random
import requests
import datetime
import sys
import time
import glob
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
with open('config/config.json', 'r') as myfile:
    CONFIG = json.load(myfile)
sys.path.append(CONFIG['REPOSITORY_PATH'])



def initialize_webdriver(headless_choice=None, download_path=None):
    global browser
    """GECKODRIVER CONFIGS"""
    gecko_executable_path = str(CONFIG['REPOSITORY_PATH'] +"\\" +CONFIG['GECKODRIVER_FILEPATH'])

    if headless_choice is None:
        headless_choice = False
    if download_path is None:
        download_path = CONFIG['REPOSITORY_PATH'] + "\\working_directory"
        if not os.path.exists(os.path.dirname(download_path)):
            os.mkdir(os.path.dirname(download_path))
        download_path = CONFIG['REPOSITORY_PATH'] + "\\working_directory\\downloads"
        if not os.path.exists(os.path.dirname(download_path)):
            os.mkdir(os.path.dirname(download_path))

    start = time.time()
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    options = Options()
    options.set_preference("browser.download.folderList", 2) # tells it not to use default Downloads directory
    options.set_preference("browser.download.manager.showWhenStarting", False) #turns of showing download progress
    options.set_preference("browser.helperApps.alwaysAsk.force",False)
    options.set_preference("browser.download.dir", download_path) #sets the directory for downloads
    options.set_preference("browser.helperApps.neverAsk.saveToDisk",  "text/plain, application/octet-stream, application/binary, text/csv, application/csv, application/excel, text/comma-separated-values, text/xml, application/xml") #tells Firefox to automatically download the files of the selected mime-types
    options.set_preference("browser.helperApps.neverAsk.saveToDisk",  "application/pdf") #tells Firefox to automatically download the files of the selected mime-types

    options.headless = headless_choice
    browser = webdriver.Firefox(executable_path=gecko_executable_path, options=options,
                                capabilities=firefox_capabilities)  # starts driver
    return browser
