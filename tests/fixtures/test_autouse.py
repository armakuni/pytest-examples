import pytest
import os


@pytest.fixture(autouse=True)
def environ_foo():
    os.environ["FOO"] = "bar"


def test_foobar():
    assert os.environ.get("FOO") == "bar"
