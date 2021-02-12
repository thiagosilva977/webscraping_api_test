import datetime
import io
import json
import logging
import logging.config
import os
import random
import string
import time
from imagetyperzapi3.imagetyperzapi import ImageTyperzAPI

with open('config/config.json', 'r') as myfile:
    CONFIG = json.load(myfile)

def solve_captcha(URL_CAPTCHA,SITEKEY):
    access_token = CONFIG['CAPTCHA_CREDENTIALS']
    ita = ImageTyperzAPI(access_token)
    recaptcha_params = {
        'page_url': URL_CAPTCHA,
        'sitekey': SITEKEY,
        'proxy': '126.45.34.53:345',
    }
    captcha_id = ita.submit_recaptcha(recaptcha_params)
    while ita.in_progress():
        time.sleep(2)
    recaptcha_response = ita.retrieve_recaptcha(captcha_id)

    return recaptcha_response
