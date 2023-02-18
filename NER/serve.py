#!/usr/bin/python
from flask import Flask
import flask
import os
#import spacy
import json
import logging
import os

import tensorflow as tf
from tensorflow import keras


#Load in model
#nlp = spacy.load('en_core_web_sm')




# The flask app for serving predictions
app = Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    status = 200 
    return flask.Response(response= '\n', status=status, mimetype='application/json')


#@app.route('/invocations', methods=['POST'])
#def transformation():
#
#    #Process input
#    input_json = flask.request.get_json()
#    resp = input_json['input']
#
#    #NER
#    doc = nlp(resp)
#    entities = [(X.text, X.label_) for X in doc.ents]
#
#    # Transform predictions to JSON
#    result = {
#        'output': entities
#        }
#
#    resultjson = json.dumps(result)
#    return flask.Response(response=resultjson, status=200, mimetype='application/json')

@app.route('/invocations', methods=['POST'])
def transformation():
    ver=tf.version.VERSION    
    # Transform predictions to JSON
    result = {
        'output': ver
        }

    resultjson = json.dumps(result)
    return flask.Response(response=resultjson, status=200, mimetype='application/json')


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
