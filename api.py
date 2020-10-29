import flask
# from flask_cors import CORS, cross_origin
import json
from flask import request, jsonify

# this is a test

app = flask.Flask(__name__)
# cors = CORS(app)
app.config["DEBUG"] = True


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
  return "<h1>To use the api, insert: '/test?pos='a number'' at the end of the url</h1>"

@app.route('/test', methods = ['GET', 'POST'])
def api_test_get():
  res = request.args
  print(request.data)
  movie = res.to_dict(flat=False)['pos'][0]
  print(movie)
  return testOutput(movie)


def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response