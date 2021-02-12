import pymongo
import datetime

def insert_into_stack_posts(ID_POST,TITLE_POST,AUTHOR_POST,TEXT_POST,DATE_POST,
                            TAGS,URL_POST):


    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = myclient['STACK_DATABASE']
    mycol= mydb['table_stack_posts']
    current_datetime = datetime.datetime.now()

    doc = {

        'ID_POST':ID_POST
        ,'TITLE_POST':TITLE_POST
        ,'AUTHOR_POST':AUTHOR_POST
        ,'TEXT_POST':TEXT_POST
        ,'DATE_POST':DATE_POST
        ,'TAGS':TAGS
        ,'URL_POST':URL_POST
        ,'INSERTION_DATE':current_datetime

    }
    mycol.insert_one(doc)

def insert_into_stack_answers(ID_POST,ID_ANSWER,ANSWER_TYPE,AUTHOR_ANSWER,TEXT_ANSWER,DATE_ANSWER):


    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = myclient['STACK_DATABASE']
    mycol= mydb['table_stack_answers']
    current_datetime = datetime.datetime.now()

    doc = {

        'ID_POST':ID_POST
        ,'ID_ANSWER':ID_ANSWER
        ,'ANSWER_TYPE':ANSWER_TYPE
        ,'AUTHOR_ANSWER':AUTHOR_ANSWER
        ,'TEXT_ANSWER':TEXT_ANSWER
        ,'DATE_ANSWER':DATE_ANSWER
        ,'INSERTION_DATE':current_datetime

    }
    mycol.insert_one(doc)

def insert_into_stack_comments(ID_POST,ID_ANSWER,ID_COMMENT,AUTHOR_COMMENT,TEXT_COMMENT,DATE_COMMENT):


    myclient = pymongo.MongoClient('mongodb://localhost:27017')
    mydb = myclient['STACK_DATABASE']
    mycol= mydb['table_stack_comments']
    current_datetime = datetime.datetime.now()

    doc = {

        'ID_POST':ID_POST
        ,'ID_ANSWER':ID_ANSWER
        ,'ID_COMMENT':ID_COMMENT
        ,'AUTHOR_COMMENT':AUTHOR_COMMENT
        ,'TEXT_COMMENT':TEXT_COMMENT
        ,'DATE_COMMENT':DATE_COMMENT
        ,'INSERTION_DATE':current_datetime

    }
    mycol.insert_one(doc)