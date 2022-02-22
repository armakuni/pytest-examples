# The moto testing framework does not accurately simulate some services, such as CodePipeline
# This file demonstrates how to construct a mock boto3 client that supplies a locally mocked
# codepipeline client whilst falling back to moto3 for other types.
from lib.codepipeline_accessor import get_pipeline_details
import pytest
from unittest import mock
import boto3
from moto import mock_s3


@pytest.fixture
def mock_boto3(codepipeline_client):
    clients = {"codepipeline": codepipeline_client}
    _orig_boto3_client = boto3.client
    with mock.patch('boto3.client') as mocked_boto3:
        mocked_boto3.side_effect = lambda client_type, **kwargs: clients.get(
            client_type, _orig_boto3_client(client_type, **kwargs))
        yield mocked_boto3


@pytest.fixture
def codepipeline_client(pipeline_name, pipeline_details):
    mock_client = mock.Mock()
    mock_client.pipeline_dict = {pipeline_name: pipeline_details}
    mock_client.get_pipeline.side_effect = lambda pn: mock_client.pipeline_dict.get(pn, {})
    return mock_client


@pytest.fixture
def mock_boto3_with_s3(mock_boto3):
    with mock_s3():
        yield mock_boto3


@pytest.fixture
def pipeline_name():
    return "mypipeline"


@pytest.fixture
def pipeline_details():
    return {"foo": "bar"}


def test_codepipeline_mock(mock_boto3, pipeline_name, pipeline_details):
    '''demonstrate getting the mocked codepipeline client'''
    client = boto3.client("codepipeline")
    details = client.get_pipeline(pipeline_name)
    assert details == pipeline_details


def test_codepipeline_mock_import(mock_boto3, pipeline_name, pipeline_details):
    '''demonstrate using the mock boto3 with a separate library'''
    details = get_pipeline_details(pipeline_name)
    assert details == pipeline_details


def test_mock_s3(mock_boto3_with_s3):
    '''demonstrate using the enhanced boto3 client'''
    s3 = boto3.client('s3', region_name='us-east-1')
    s3.create_bucket(Bucket='mybucket')
    result = s3.list_buckets()
    names = [x['Name'] for x in result['Buckets']]
    assert names == ['mybucket']
