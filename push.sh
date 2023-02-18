#!/usr/bin/bash
docker build  --platform linux/amd64 -t youree-dev-ecr-model  .
docker tag  youree-dev-ecr-model 323423043710.dkr.ecr.us-east-1.amazonaws.com/youree-dev-ecr-model:latest
docker push  323423043710.dkr.ecr.us-east-1.amazonaws.com/youree-dev-ecr-model:latest
