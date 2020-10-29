import flask
import json
from flask import request, jsonify

# this is a test

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", '*');
    res.header("Access-Control-Allow-Credentials", true);
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header("Access-Control-Allow-Headers", 'Origin,X-Requested-With,Content-Type,Accept,content-type,application/json');
    next();
})

def testOutput(name):
  with open('movies.json') as f:
    data = json.load(f)

  return_value = 0
  for movie in data:
    if movie['rank'] == name:
      return_value = movie

  return jsonify(return_value)

@app.route('/', methods=['GET'])
def home():
  return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/test', methods = ['GET', 'POST'])
def api_test_get():
  res = request.args
  print(request.data)
  movie = res.to_dict(flat=False)['pos'][0]
  print(movie)
  return testOutput(movie)
