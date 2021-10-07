import pytest


@pytest.fixture
def db():
    db = DB({"foo": "bar"})
    yield(db)
    db.close()


def test_db(db):
    assert db.find("foo") == "bar"


class DB():
    def __init__(self, content):
        self.content = content

    def close(self):
        self.content = {}

    def find(self, key):
        return self.content[key]
