# aws_cdk_multi-region
AWS CDK deploy to multi-region PoC

This will create a AWS SSM parameter called **FooParameter** in *us-east-1* and *eu-west-1* AWS regions, and then destroy it.


The [**.aws_credentials**](.aws_credentials) contains the AWS Credentials
```angular2html
[default]
aws_access_key_id=AWS_ACCESS_KEY
aws_secret_access_key=AWS_SECRET_KEY
```

To run:
```
DOCKER_BUILDKIT=1 docker build -t aws_cdk_multi-region --secret id=aws,src=.aws_credentials .
```

The container will run the contents of [**bootstrap.sh**](bootstrap.sh) 

To list the stacks:
```angular2html
$ cd awscdk_poc
$ cdk list
AwscdkPocStack-eu
AwscdkPocStack-us
```
