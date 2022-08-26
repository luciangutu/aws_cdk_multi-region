#!/bin/bash

# cdk init app --language python
source .venv/bin/activate
python3 -m pip install -r requirements.txt
#ACCOUNT_ID=$(aws sts get-caller-identity --query 'Account' --output text)
#AWS_PRIMARY_REGION=us-east-1
#AWS_SECONDARY_REGION=eu-west-1
#for region in $AWS_PRIMARY_REGION $AWS_SECONDARY_REGION
#do
#  cdk bootstrap aws://$ACCOUNT_ID/$region
#done
cdk bootstrap --all
for stack in $(cdk list)
do
  cdk synth $stack
done
cdk deploy --all
cdk destroy --all
