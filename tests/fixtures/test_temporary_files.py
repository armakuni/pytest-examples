import pytest


@pytest.fixture
def contents():
    return "The quick brown fox"


@pytest.fixture
def config_file(tmp_path, contents):
    file = tmp_path / "foo.json"
    try:
        file.write_text(contents)
        yield (str(file))
    finally:
        file.unlink()


def test_temp_file(config_file, contents):
    found = open(config_file, "r").read()
    assert found == contents
