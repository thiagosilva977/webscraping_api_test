import json
import sys
import logging
import datetime
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
with open('config/config.json', 'r') as myfile:
    CONFIG = json.load(myfile)
sys.path.append(CONFIG['REPOSITORY_PATH'])
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='./working_directory/webscraping_logs.log', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())
import string
import random

import common.selenium_functions as selenium_function
import common.captcha_solver as captcha_function
import common.database_functions as database_function

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))


def content_parser_and_export_data(post_url):

    #Generates a random code for ID POST
    post_code = id_generator()
    #post_url = 'https://stackoverflow.com/questions/11804148/parsing-html-to-get-text-inside-an-element'
    #post_url = 'https://stackoverflow.com/questions/66175822/how-can-i-validate-a-list-index-as-an-integer'
    html_text = requests.get(post_url).text
    soup = BeautifulSoup(html_text, 'html.parser')


    ####### ABOUT MAIN QUESTION

    titulo = soup.find("h1", class_="fs-headline1 ow-break-word mb8 grid--cell fl1").text
    post_soup = soup.find('div', {'class': 'post-layout'})
    post_text = post_soup.find('div', {'class': 's-prose js-post-body'}).text
    post_author = post_soup.find('span', {'class': 'd-none', 'itemprop': 'name'}).text
    post_time = post_soup.find('span', {'class': 'relativetime'}).text

    print(titulo)
    print(post_text)
    print(post_author)
    print(post_time)

    #GET TAGS
    post_tags = ''
    tags = post_soup.find_all('a', {'rel': 'tag'})
    for ul in tags:
        current_tag = ul.text
        post_tags = str(post_tags +'/'+current_tag)

    print(post_tags)


    #Insert into database
    database_function.insert_into_stack_posts(post_code,titulo,post_author,str(post_text),
                                              post_time,post_tags,post_url)

    # Get comments id
    # get ID of comment
    comments_post = \
    post_soup.find('div', {'class': 'post-layout--right js-post-comments-component'}).findNext('div').attrs[
        'data-post-id']

    # make an request with id
    response_comments = requests.get('https://stackoverflow.com/posts/' + str(comments_post) + '/comments?_').text
    soup_owner_post_comments = BeautifulSoup(response_comments, 'html.parser')

    all_comments_post = soup_owner_post_comments.find_all('span', {'class': 'comment-copy'})

    for ul in all_comments_post:
        comment_code = id_generator()
        current_comment_originalpost = ul.text
        current_owner_comment_originalpost = ul.findNext('a').text
        current_data_comment_originalpost = ul.findNext('a').findNext('span').findNext('span').text

        print(current_comment_originalpost)
        print(current_owner_comment_originalpost)
        print(current_data_comment_originalpost)

        #Insert into comments table
        database_function.insert_into_stack_comments(post_code,None,comment_code,current_owner_comment_originalpost,
                                                     current_comment_originalpost,current_data_comment_originalpost)

        print('\n\n')


    try:
        ####### ABOUT ACCEPTED ANSWER

        answer_accepted_code = id_generator()

        accepted_answer = soup.find('div', {'itemprop': 'acceptedAnswer'})
        accepted_answer_text = accepted_answer.find('div', {'class': 's-prose js-post-body'}).text
        accepted_answer_author = accepted_answer.find('span', {'class': 'd-none','itemprop':'name'}).text
        accepted_answer_time = accepted_answer.find('span', {'class': 'relativetime'}).text

        print(accepted_answer_text)
        print(accepted_answer_author)
        print(accepted_answer_time)

        database_function.insert_into_stack_answers(post_code,answer_accepted_code,'ACCEPTED_ANSWER',accepted_answer_author,
                                                    accepted_answer_text,accepted_answer_time)

        #Get comments id
        # get ID of comment
        comments_post = accepted_answer.find('div', {'class': 'post-layout--right js-post-comments-component'}).findNext('div').attrs[
            'data-post-id']
        # make an request with id
        response_comments = requests.get('https://stackoverflow.com/posts/' + str(comments_post) + '/comments?_').text
        soup_owner_post_comments = BeautifulSoup(response_comments, 'html.parser')

        all_comments_post = soup_owner_post_comments.find_all('span', {'class': 'comment-copy'})

        for ul in all_comments_post:
            comment_code = id_generator()

            current_comment_originalpost = ul.text
            current_owner_comment_originalpost = ul.findNext('a').text
            current_data_comment_originalpost = ul.findNext('a').findNext('span').findNext('span').text

            print(current_comment_originalpost)
            print(current_owner_comment_originalpost)
            print(current_data_comment_originalpost)

            database_function.insert_into_stack_comments(post_code,answer_accepted_code,comment_code,
                                                         current_owner_comment_originalpost,current_comment_originalpost,
                                                         current_data_comment_originalpost)

            print('\n\n')

    except:
        pass

    try:
        ####### ABOUT SUGGESTED ANSWER

        suggested_answer = soup.find_all('div', {'itemprop': 'suggestedAnswer'})

        for any_answer in suggested_answer:
            suggested_answer_code = id_generator()

            suggested_answer_text = any_answer.find('div', {'class': 's-prose js-post-body'}).text
            suggested_answer_author = any_answer.find('span', {'class': 'd-none', 'itemprop': 'name'}).text
            suggested_answer_time = any_answer.find('span', {'class': 'relativetime'}).text

            print(suggested_answer_text)
            print(suggested_answer_author)
            print(suggested_answer_time)

            database_function.insert_into_stack_answers(post_code, answer_accepted_code, 'SUGGESTED_ANSWER',
                                                        suggested_answer_author,
                                                        suggested_answer_text, suggested_answer_time)

            # get ID of comment
            comments_post = \
                any_answer.find('div', {'class': 'post-layout--right js-post-comments-component'}).findNext('div').attrs[
                    'data-post-id']
            # make an request with id
            response_comments = requests.get('https://stackoverflow.com/posts/' + str(comments_post) + '/comments?_').text
            soup_owner_suggested_post_comments = BeautifulSoup(response_comments, 'html.parser')

            all_comments_post = soup_owner_suggested_post_comments.find_all('span', {'class': 'comment-copy'})
            for ul in all_comments_post:
                comment_code = id_generator()
                current_comment_originalpost = ul.text
                current_owner_comment_originalpost = ul.findNext('a').text
                current_data_comment_originalpost = ul.findNext('a').findNext('span').findNext('span').text

                print(current_comment_originalpost)
                print(current_owner_comment_originalpost)
                print(current_data_comment_originalpost)

                database_function.insert_into_stack_comments(post_code,suggested_answer_code,comment_code,
                                                             current_owner_comment_originalpost,current_comment_originalpost,
                                                             current_data_comment_originalpost)

                print('\n\n')
    except:
        pass


if __name__ == '__main__':
    """The main script for web-scraping"""
    #Some configs
    key_search = "Python"
    maximum_pages_search = 2

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
        # I didn't continue because it may take a lot of time and $10, but I filtered the all questions by python term :)
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

        url_list = []

        #First of all: Create a page-changer engine
        for i in range(maximum_pages_search):
            list_of_elements = browser.find_elements_by_class_name('question-hyperlink')

            for j in range(len(list_of_elements)):
                current_url = list_of_elements[j].get_attribute('href')
                print(current_url)
                url_list.append(current_url)




            browser.find_element_by_xpath('//a[@class="s-pagination--item js-pagination-item"]').click()
            time.sleep(5)


        browser.quit()

        # END OF SELENIUM WORK
        # Now its time to use BS4 to get and parse all information.
        for i in range(len(url_list)):
            content_parser_and_export_data(url_list[i])

        #Finished the parsing and database insertions.

        #Now its time to use the API




    except BaseException:
        logging.exception(BaseException)
