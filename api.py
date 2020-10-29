import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def testOutput(age):
  return jsonify([{'name': 'fred', 'age': age}])

@app.route('/favicon.ico')
def fav()
  return "<h1>What is this?</h1>"

@app.route('/', methods=['GET'])
def home():
  return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/test', methods = ['GET', 'POST'])
def api_test_get():
  print("=====")
  print(request.method)
  print(request.data)
  print(request.get_json())
  print("$$$$$$    $$$$$$$$")
  return jsonify(request.args)
