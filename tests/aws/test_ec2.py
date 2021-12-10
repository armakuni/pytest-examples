import boto3
from moto import mock_ec2


@mock_ec2
def test_add_servers():
    client = boto3.client("ec2", region_name="us-west-1")
    ami_id = client.describe_images()["Images"][0]["ImageId"]

    add_servers(ami_id, 2)

    client = boto3.client("ec2", region_name="us-west-1")
    instances = client.describe_instances()["Reservations"][0]["Instances"]
    assert len(instances) == 2
    instance1 = instances[0]
    assert instance1["ImageId"] == ami_id


def add_servers(ami_id, count):
    client = boto3.client("ec2", region_name="us-west-1")
    client.run_instances(ImageId=ami_id, MinCount=count, MaxCount=count)
