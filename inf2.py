#!/usr/bin/python
import os
import io
import boto3
import json
import csv

# grab environment variables
ENDPOINT_NAME =  'youree-dev-sage-endpoint'
runtime= boto3.client('runtime.sagemaker')
content_type = "application/json"

def lambda_handler(event, context):
   request_body = event
   # grab environment variables
   ENDPOINT_NAME =  'youree-dev-sage-endpoint'
   runtime= boto3.client('runtime.sagemaker')
   data = json.loads(json.dumps(request_body))
   payload = json.dumps(data)
   response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType=content_type,
                                       Body=payload)
   result = json.loads(response['Body'].read().decode())['output']
       res ={
        "statusCode": 200,
        "headers": {
            "Content-Type": "*/*"
        },
        "body" : result
    };

   return res

