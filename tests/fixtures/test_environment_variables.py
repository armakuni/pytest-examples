import pytest
import os
from unittest import mock


@pytest.fixture
def env_creds():
    with mock.patch.dict(os.environ, {
        "CRED_USERNAME": "fred",
        "CRED_PASSWORD": "secret"
    }):
        yield


def test_creds(env_creds):
    assert os.environ.get("CRED_USERNAME") == "fred"
    assert os.environ.get("CRED_PASSWORD") == "secret"


def test_creds_unset():
    assert os.environ.get("CRED_USERNAME") is None
    assert os.environ.get("CRED_PASSWORD") is None
