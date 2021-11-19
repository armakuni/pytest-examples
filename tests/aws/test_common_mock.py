import pytest
import boto3
from moto import mock_ec2


@pytest.fixture
def ec2():
    """Example of how to use a common EC2 mock across fixtures and tests

    a common mistake is to use the @mock_ec2 decorator with fixture and with test,
    but this will cause a new mock EC2 to be created, and they don't share state.
    """
    with mock_ec2():
        yield


@pytest.fixture
def ami_id(ec2):
    client = boto3.client("ec2", region_name="us-west-1")
    return client.describe_images()["Images"][0]["ImageId"]


def test_add_servers(ec2, ami_id):
    add_servers(ami_id, 2)

    client = boto3.client("ec2", region_name="us-west-1")
    instances = client.describe_instances()["Reservations"][0]["Instances"]
    assert len(instances) == 2
    instance1 = instances[0]
    assert instance1["ImageId"] == ami_id


def add_servers(ami_id, count):
    client = boto3.client("ec2", region_name="us-west-1")
    client.run_instances(ImageId=ami_id, MinCount=count, MaxCount=count)
