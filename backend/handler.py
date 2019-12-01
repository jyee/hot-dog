import boto3
from datadog_lambda.wrapper import datadog_lambda_wrapper
import json
import requests

@datadog_lambda_wrapper
def hotdogsave(event, context):
    body = json.loads(event["body"])
    dog = body["dog"]
    filename = dog[dog.rfind("/")+1:]

    r = requests.get(dog, allow_redirects = True)

    s3 = boto3.client('s3', region_name = 'us-east-1')
    #response = s3.upload_fileobj(r.content, "hot-dog-saves", filename)
    response = s3.put_object(
        Bucket='hot-dog-saves',
        Body=r.content,
        Key=filename
    )

    print(json.dumps(response))

    response = {
        "statusCode": 200,
        "body": json.dumps(response)
    }

    return response
