import aws_cdk as core
import aws_cdk.assertions as assertions

from awscdk_poc.awscdk_poc_stack import AwscdkPocStack

# example tests. To run these tests, uncomment this file along with the example
# resource in awscdk_poc/awscdk_poc_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwscdkPocStack(app, "awscdk-poc")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
