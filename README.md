# Sage-Maker-Endpoint-Docker
---

## Table of Contents
---
- [Description](#description)
- [Prerequisite](#Prerequisites)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Examples](#examples)
  - [Env_Vars](#Env_Vars)
  - [Help](#Help)
- [Contributing](#contributing)
- [Testing](#testing)
  
- [Deployment](#deployment)
   - [Build](#Build)
- [Documentation](#documentation)
- [Changelog](#changelog)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact_Information](#Contact_Information)

## Description
---

##  Prerequisite
---

## Getting Started
---
To get started, follow these steps:
1. : What to do
   
   `cmd`
   // Insert code example here
   
3. : What to do
   
   `cmd`

   ### Prerequisites
   ### Installation

## Usage
---

### Configuration
1. : What to do
   
   `cmd`

3. : What to do

   `cmd`
   ### Examples
   ### Env_Vars
| ENV VAR Name | Description | Values | 
|--------------|:-----------:|:------:|
|  SECRET_KEY         |    User acces key value to auth to api |xxxx
|  ACCESS_KEY         |    User secret key value to auth to api|xxxx


   ### Help

## Contributing
---

## Testing
---

## Deployment
---
### Build

## Documentation
---

## Changelog
---

## License
---
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
---

### Contact_Information
 E-mail: maher.naija@gmail.com



   



To deploy the docker image to ECR:

region=${region:-us-east-1}\
account=$(aws sts get-caller-identity --query Account --output text)\
algorithm_name=sm-pretrained-spacy\
account=$(aws sts get-caller-identity --query Account --output text)\



aws ecr get-login-password --region $region|docker login --username AWS --password-stdin ${fullname}\
 docker build  --platform linux/amd64 -t ${algorithm_name} \
 docker tag ${algorithm_name} ${fullname} \
 docker push ${fullname} \
