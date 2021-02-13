from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'STACK_DATABASE'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/STACK_DATABASE'  # Change the localhost port if doesn't work

mongo = PyMongo(app)


@app.route('/table_stack_posts', methods=['GET'])
def get_all_posts():
    """This route returns the whole table of posts"""
    posts = mongo.db.table_stack_posts
    output = []
    for item in posts.find():
        output.append({'id_post': item['ID_POST'], 'title_post': item['TITLE_POST']
                          , 'author_post': item['AUTHOR_POST'], 'text_post': item['TEXT_POST']
                          , 'date_post': item['DATE_POST'], 'tags': item['TAGS'], 'url_post': item['URL_POST']
                          , 'insertion_date': item['INSERTION_DATE']

                       })
    return jsonify({'result': output})


@app.route('/table_stack_answers', methods=['GET'])
def get_all_answers():
    """This route returns the whole table of answers of posts"""

    posts = mongo.db.table_stack_answers
    output = []
    for item in posts.find():
        output.append({'id_post': item['ID_POST'], 'id_answer': item['ID_ANSWER']
                          , 'answer_type': item['ANSWER_TYPE'], 'author_answer': item['AUTHOR_ANSWER']
                          , 'text_answer': item['TEXT_ANSWER'], 'date_answer': item['DATE_ANSWER'],
                       'insertion_date': item['INSERTION_DATE']
                       })
    return jsonify({'result': output})


@app.route('/table_stack_comments', methods=['GET'])
def get_all_comments():
    """This route returns the whole table of commentaries"""

    posts = mongo.db.table_stack_comments
    output = []
    for item in posts.find():
        output.append({'id_post': item['ID_POST'], 'id_answer': item['ID_ANSWER']
                          , 'id_comment': item['ID_COMMENT'], 'author_comment': item['AUTHOR_COMMENT']
                          , 'text_comment': item['TEXT_COMMENT'], 'date_comment': item['DATE_COMMENT'],
                       'insertion_date': item['INSERTION_DATE']
                       })
    return jsonify({'result': output})


@app.route('/search_name', methods=['GET'])
def search_name():
    """This route returns the results of name search"""

    username = request.form.get("autor")
    if username == None:
        username = request.args.get('autor')

    if '%' in username:
        username = username.replace('%', ' ')

    output_query_posts = []
    output_query_answers = []
    output_query_comments = []

    # query: posts
    myquery_post = {"AUTHOR_POST": username}
    mydoc_posts = mongo.db.table_stack_posts.find(myquery_post)

    for x in mydoc_posts:
        results = {
            "id_post": x.get('ID_POST'),
            "title_post": x.get('TITLE_POST'),
            "author_post": x.get('AUTHOR_POST'),
            "text_post": x.get('TEXT_POST'),
            "date_post": x.get('DATE_POST'),
            "tags": x.get('TAGS'),
            "url_post": x.get('URL_POST'),
            "insertion_date": x.get('INSERTION_DATE'),
        }
        output_query_posts.append(results)

    # query: answers
    myquery_answer = {"AUTHOR_ANSWER": username}
    mydoc_answer = mongo.db.table_stack_answers.find(myquery_answer)
    for x in mydoc_answer:
        results = {
            "id_post": x.get('ID_POST'),
            "id_answer": x.get('ID_ANSWER'),
            "answer_type": x.get('ANSWER_TYPE'),
            "author_answer": x.get('AUTHOR_ANSWER'),
            "text_answer": x.get('TEXT_ANSWER'),
            "date_answer": x.get('DATE_ANSWER'),
            "insertion_date": x.get('INSERTION_DATE'),
        }
        output_query_answers.append(results)

    # query: comments
    myquery_comments = {"AUTHOR_COMMENT": username}
    mydoc_comment = mongo.db.table_stack_comments.find(myquery_comments)
    for x in mydoc_comment:
        results = {
            "id_post": x.get('ID_POST'),
            "id_answer": x.get('ID_ANSWER'),
            "id_comment": x.get('ID_COMMENT'),
            "author_comment": x.get('AUTHOR_COMMENT'),
            "text_comment": x.get('TEXT_COMMENT'),
            "date_comment": x.get('DATE_COMMENT'),
            "insertion_date": x.get('INSERTION_DATE'),
        }
        output_query_comments.append(results)

    return jsonify({'posts': output_query_posts, 'answers': output_query_answers, 'comments': output_query_comments})


if __name__ == '__main__':
    app.run(debug=True)
