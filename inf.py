#!/usr/bin/python



content_type = "application/json"
request_body = {"input": "This is a test with NER in America with Amazon and Microsoft in Seattle, writing random stuff."}
endpoint_name = 'youree-dev-sage-endpoint'
print('Endpoint name: ' + endpoint_name)

import json
import boto3
from sagemaker import get_execution_role

sm_client = boto3.client(service_name='sagemaker')
runtime_sm_client = boto3.client(service_name='sagemaker-runtime')



#Serialize data for endpoint
data = json.loads(json.dumps(request_body))
payload = json.dumps(data)

#Endpoint invocation
response = runtime_sm_client.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType=content_type,
    Body=payload)

print(response)
#Parse results
result = json.loads(response['Body'].read().decode())['output']




print(result)
