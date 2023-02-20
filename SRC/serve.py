#!/usr/bin/python
from flask import Flask
import flask
import os
import json
import logging
import os
import numpy as np

import tensorflow as tf
from tensorflow import keras

# The flask app for serving predictions
app = Flask(__name__)
@app.route('/ping', methods=['GET'])
def ping():
    # Check if the classifier was loaded correctly
    status = 200 
    return flask.Response(response= '\n', status=status, mimetype='application/json')



@app.route('/invocations', methods=['POST'])
def transformation():
    input_json = flask.request.get_json()
    print(input_json)
    ent=input_json["input"]
    print(ent)
    model = tf.keras.models.load_model('/opt/ml/model/mobilenet_v2.h5')
    x_input = np.array([ent])
    res=str(model.predict(x_input, batch_size=128)[0][0])
    # Transform predictions to JSON
    result = {
        'output': res
        }

    resultjson = json.dumps(result)
    return flask.Response(response=resultjson, status=200, mimetype='application/json')


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
