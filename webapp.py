from flask import Flask, jsonify, make_response, render_template, redirect, request, abort, redirect, url_for
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/api/docs'
API_URL = '/static/openapi.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint)

@app.route('/')
def index():
    return redirect('/api/docs')

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

