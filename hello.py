from flask import Flask, jsonify, make_response, render_template
from markupsafe import escape
from flask import request
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get/<userId>', methods=['GET'])
def firstRoute(userId):
    query = request.args
    return f"query: {query.to_dict()}\npath: userId = {userId}"

@app.route('/post', methods=['POST'])
def secondRoute():
    query = request.args
    body = request.json
    return f"query: {query.to_dict()}\nbody: {body}"

@app.route('/head', methods=['HEAD'])
def thirdRoute():
    return ''

@app.route('/options', methods=['OPTIONS'])
def fourRoute():
    response = make_response('', 200)
    response.headers['Allow'] = 'OPTIONS, HEAD'
    return response

