import pytest

# Using this global variable to show that super_expensive_db fixture is only called once
scoped_hit_count = 0


@pytest.fixture(scope="module")
def super_expensive_db():
    global scoped_hit_count
    scoped_hit_count += 1
    pretend_db = {"hits": scoped_hit_count}
    yield(pretend_db)


def test_scoped_db_1(super_expensive_db):
    assert super_expensive_db["hits"] == 1


def test_scoped_db_2(super_expensive_db):
    assert super_expensive_db["hits"] == 1
