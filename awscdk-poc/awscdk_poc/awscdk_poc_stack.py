from aws_cdk import (
    Stack,
    aws_ssm as ssm
)
from constructs import Construct


class AwscdkPocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AwscdkPocQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        ssm.StringParameter(self, "cdk-poc",
                            description="The value Foo",
                            parameter_name="FooParameter",
                            string_value="Foo"
                            )

