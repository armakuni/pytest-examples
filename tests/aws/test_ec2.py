import boto3
from moto import mock_ec2


@mock_ec2
def test_add_servers():
    add_servers('ami-1234abcd', 2)

    client = boto3.client('ec2', region_name='us-west-1')
    instances = client.describe_instances()['Reservations'][0]['Instances']
    assert len(instances) == 2
    instance1 = instances[0]
    assert instance1['ImageId'] == 'ami-1234abcd'


def add_servers(ami_id, count):
    client = boto3.client('ec2', region_name='us-west-1')
    client.run_instances(ImageId=ami_id, MinCount=count, MaxCount=count)
