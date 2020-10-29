import flask
import json
from flask import request, jsonify

# this is a test

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def testOutput(age):
  with open('movies.json') as f:
    data = json.load(f)
  return jsonify(data)

@app.route('/', methods=['GET'])
def home():
  return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/test', methods = ['GET', 'POST'])
def api_test_get():
  return testOutput(0)
