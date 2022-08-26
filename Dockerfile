FROM node
ENV AWS_REGION="us-east-1"

RUN apt-get update -y && \
    apt-get install -y unzip wget

################################
# Install python
################################
RUN apt-get install -y python3-pip jq
RUN pip3 install --upgrade pipenv
RUN python3 -m pip install aws-cdk-lib awscli

################################
# Install CDK
################################
RUN npm install -g aws-cdk

#ADD ${PROJECT_NAME}/ ${PROJECT_NAME}
#WORKDIR ${PROJECT_NAME}
#RUN pip3 install -r requirements.txt

COPY bootstrap.sh .
RUN chmod +x bootstrap.sh
RUN --mount=type=secret,id=aws,target=/root/.aws/credentials ./bootstrap.sh
