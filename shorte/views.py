from flask import render_template, request, Response
from shorte import app
import json

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/g')
def generate():
    data = {'short_url': 'HELLO'}
    data = json.dumps(data)
    response = Response()
    response.status_code = 200
    response.mimetype = 'application/json'
    response.data = data
    return response
