import flask
import json
import sqlite3
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

conn = sqlite3.connect('db/jukebox.sqlite')
c = conn.cursor()


def testOutput(name):
  with open('movies.json') as f:
    data = json.load(f)
  return_value = 0
  for movie in data:
    if movie['rank'] == name:
      return_value = movie

  return build_actual_response(jsonify(return_value))

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/movie', methods = ['GET', 'POST'])
def api_test_get():
  res = request.args
  print(request.data)
  movie = res.to_dict(flat=False)['pos'][0]
  print(movie)
  return testOutput(movie)

@app.route('/artists', methods = ['GET', 'POST'])
def db_get_artists():
  result = []
  arr = c.execute("SELECT * FROM artists")
  for row in arr:
    result.append({row[0]: row[1]})

  return build_actual_response(jsonify(result))

@app.route('/uningo', methods = ['GET'])
def db_get_artists():
  result = []
  arr = cursor.execute("SELECT * FROM stblcountry")
  for row in arr:
    result.append({row[0]: row[1]})

  return build_actual_response(jsonify(result))


# def build_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin", "*")
#     response.headers.add('Access-Control-Allow-Headers', "*")
#     response.headers.add('Access-Control-Allow-Methods', "*")
#     return response

def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response