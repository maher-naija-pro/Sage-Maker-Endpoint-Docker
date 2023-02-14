#!/usr/bin/python
from flask import Flask
import flask
import spacy
import os
import json
import logging



# The flask app for serving predictions
app = Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    status = 200 
    return flask.Response(response= '\n', status=status, mimetype='application/json')


@app.route('/invocations', methods=['POST'])
def transformation():
    
    # Transform predictions to JSON
    result = {
        'output': "ddddd"
        }

    resultjson = json.dumps(result)
    return flask.Response(response=resultjson, status=200, mimetype='application/json')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
