import boto3


def get_pipeline_details(pipeline_name):
    client = boto3.client("codepipeline")
    print(client)
    return client.get_pipeline(pipeline_name)
