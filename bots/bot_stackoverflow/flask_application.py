from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import json
app = Flask(__name__)
import json
from bson import json_util
app.config['MONGO_DBNAME'] = 'STACK_DATABASE'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/STACK_DATABASE'

mongo = PyMongo(app)

from bson.objectid import ObjectId

@app.route('/table_stack_posts', methods=['GET'])
def get_all_posts():
  posts = mongo.db.table_stack_posts
  output = []
  for item in posts.find():
    output.append({'id_post' : item['ID_POST'], 'title_post' : item['TITLE_POST']
                  , 'author_post': item['AUTHOR_POST'], 'text_post' : item['TEXT_POST']
                  , 'date_post': item['DATE_POST'], 'tags' : item['TAGS'], 'url_post' : item['URL_POST']
                    , 'insertion_date': item['INSERTION_DATE']

                   })
  return jsonify({'result' : output})



@app.route('/table_stack_answers', methods=['GET'])
def get_all_answers():
  posts = mongo.db.table_stack_answers
  output = []
  for item in posts.find():
    output.append({'id_post' : item['ID_POST'], 'id_answer' : item['ID_ANSWER']
                  , 'answer_type': item['ANSWER_TYPE'], 'author_answer' : item['AUTHOR_ANSWER']
                  , 'text_answer': item['TEXT_ANSWER'], 'date_answer' : item['DATE_ANSWER'],
                   'insertion_date' : item['INSERTION_DATE']
                   })
  return jsonify({'result' : output})




@app.route('/table_stack_comments', methods=['GET'])
def get_all_comments():
  posts = mongo.db.table_stack_comments
  output = []
  for item in posts.find():
    output.append({'id_post' : item['ID_POST'], 'id_answer' : item['ID_ANSWER']
                  , 'id_comment': item['ID_COMMENT'], 'author_comment' : item['AUTHOR_COMMENT']
                  , 'text_comment': item['TEXT_COMMENT'], 'date_comment' : item['DATE_COMMENT'],
                   'insertion_date' : item['INSERTION_DATE']
                   })
  return jsonify({'result' : output})












"""@app.route('/table_stack_posts/', methods=['GET'])
def get_one_star(name):
  star = mongo.db.stars
  s = star.find_one({'name' : name})
  if s:
    output = {'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})"""

"""@app.route('/table_stack_posts', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})"""

if __name__ == '__main__':
    app.run(debug=True)
