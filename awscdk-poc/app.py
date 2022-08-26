#!/usr/bin/env python3
import aws_cdk as cdk
from awscdk_poc.awscdk_poc_stack import AwscdkPocStack

app = cdk.App()
AwscdkPocStack(app, "AwscdkPocStack-eu", env=cdk.Environment(region="eu-west-1"))
AwscdkPocStack(app, "AwscdkPocStack-us", env=cdk.Environment(region="us-east-1"))

app.synth()
