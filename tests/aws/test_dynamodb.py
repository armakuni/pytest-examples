from moto import mock_dynamodb2
import boto3
import pytest


@pytest.fixture
def table_name():
    return "mytable"


@pytest.fixture
def dynamodb():
    """Common dynamodb context"""
    with mock_dynamodb2():
        yield


@pytest.fixture
def dynamodb_table(dynamodb, table_name):
    # resource is easier to work with than client
    conn = boto3.resource("dynamodb")
    table = conn.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
    )
    return table


def test_dynamodb(dynamodb, dynamodb_table, table_name):
    add_record(table_name, "foo", "bar")

    item = dynamodb_table.get_item(Key={"id": "foo"})
    assert item["Item"]["value"] == "bar"


def add_record(table_name, id, value):
    conn = boto3.resource("dynamodb")
    table = conn.Table(table_name)
    table.put_item(Item={"id": id, "value": value})
