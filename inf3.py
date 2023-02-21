#!/usr/bin/python
import os
import io
import boto3
import json
import csv

request_body = {"input": [1,2,3,4,5]}
# grab environment variables
ENDPOINT_NAME =  'youree-dev-sage-endpoint'
runtime= boto3.client('runtime.sagemaker')
content_type = "application/json"
data = json.loads(json.dumps(request_body))
payload = json.dumps(data)
response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType=content_type,
                                       Body=payload)
result = json.loads(response['Body'].read().decode())['output']
print(result)

