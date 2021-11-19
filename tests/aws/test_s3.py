import boto3
from moto import mock_s3


@mock_s3
def test_s3_save_and_read():
    conn = boto3.resource("s3", region_name="us-east-1")
    conn.create_bucket(Bucket="mybucket")

    write_s3("mybucket", "pytest", "is awesome")

    body = conn.Object("mybucket", "pytest").get()["Body"].read().decode("utf-8")

    assert body == "is awesome"


def write_s3(bucket, key, content):
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.put_object(Bucket=bucket, Key=key, Body=content)
