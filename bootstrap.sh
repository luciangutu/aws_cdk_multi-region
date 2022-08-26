#!/bin/bash

# cdk init app --language python
source .venv/bin/activate
python -m pip install -r requirements.txt
cdk bootstrap
cdk synth
cdk deploy
cdk destroy

