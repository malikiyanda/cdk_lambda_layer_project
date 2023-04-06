from aws_cdk import (
    Stack,
    aws_lambda as function_lambda
)
from constructs import Construct


class ResourceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Define your Lambda layer
        my_layer = function_lambda.LayerVersion(self, "SqlAlchemyLayer",
        code=function_lambda.Code.from_asset("./lambda_layers"),
        compatible_runtimes=[function_lambda.Runtime.PYTHON_3_9],
        description="A layer for SqlAlchemy")
        
        # Create your Lambda function and include the layer reference
        function = function_lambda.Function(self,
                                            "DemoCDKGITHUBLambda",
                                            function_name="codepipeline_lambda",
                                            runtime=function_lambda.Runtime.PYTHON_3_9,
                                            code=function_lambda.Code.from_asset('./lambda_code'),
                                            handler="lambda_handler.lambda_handler",
                                            layers=[my_layer]
                                            )