import pytest
import os
from unittest import mock


@pytest.fixture
def env_creds():
    # patched os.environ that will not pollute other tests
    with mock.patch.dict(
        os.environ, {"CRED_USERNAME": "fred", "CRED_PASSWORD": "secret"}
    ):
        yield


def test_creds(env_creds):
    assert os.environ.get("CRED_USERNAME") == "fred"
    assert os.environ.get("CRED_PASSWORD") == "secret"


def test_creds_unset():
    assert os.environ.get("CRED_USERNAME") is None
    assert os.environ.get("CRED_PASSWORD") is None


@pytest.fixture
def more_creds(env_creds):
    # pre-patched os.environ can be extended
    os.environ["EXTRA_CRED"] = "someothersecret"


def test_more_environment_variables(more_creds):
    assert os.environ.get("EXTRA_CRED") == "someothersecret"
    assert os.environ.get("CRED_USERNAME") == "fred"
