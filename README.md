# sage-maker-endpoint-docker

To deploy the docker image to ECR:

region=${region:-us-east-1}\
account=$(aws sts get-caller-identity --query Account --output text)\
algorithm_name=sm-pretrained-spacy\
account=$(aws sts get-caller-identity --query Account --output text)\



aws ecr get-login-password --region $region|docker login --username AWS --password-stdin ${fullname}\
 docker build  --platform linux/amd64 -t ${algorithm_name} \
 docker tag ${algorithm_name} ${fullname} \
 docker push ${fullname} \
