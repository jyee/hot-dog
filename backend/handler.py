import boto3
from datadog_lambda.wrapper import datadog_lambda_wrapper
import json
import requests

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

@datadog_lambda_wrapper
def hotdogsave(event, context):
    body = json.loads(event["body"])
    dog = body["dog"]
    filename = dog[dog.rfind("/")+1:]

    if "terrier" in dog:
        code = 500
        message = "WOOF! No terriers allowed!"
        logger.exception(message)
        raise Exception(message)
    else:
        code = 200
        message = "Here's where we should save {} to an S3 bucket".format(filename)
        logger.info(message)

    return {
        "statusCode": code,
        "body": message
    }
