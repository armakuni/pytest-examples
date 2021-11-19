from unittest import mock
import pytest


class Item():
    def __init__(self):
        self._price = 4

    def price(self):
        return self._price

    def total_price(self, units):
        return self._price * units


@mock.patch.object(Item, 'price', return_value=5)
def test_mocking_object_method_with_return_value(mock_price):
    item = Item()
    assert item.price() == 5


def test_mocking_object_method():
    item = Item()
    with mock.patch.object(item, 'price', return_value=5):
        assert item.price() == 5
    assert item.price() == 4


# This test shows how to mock the constructor to always return a particular object
def test_mock_constructor():
    with mock.patch('test_mock_classes.Item', autospec=True) as mock_item:
        mock_item.return_value = mock_item
        mock_item.price.return_value = 10
        item = Item()
        assert item.price() == 10


# This test demonstrate how to bolt original class methods onto your mock object. It makes
# use of the convenient malleability of the "self" parameter.
@pytest.fixture
def mock_item():
    orig_item_class = Item  # otherwise we will recurse with patched Item
    with mock.patch('test_mock_classes.Item', autospec=True) as the_mock:
        the_mock.return_value = the_mock
        the_mock.total_price.side_effect = lambda units: orig_item_class.total_price(
            the_mock, units)
        yield the_mock


def test_mock_constructor_wrap_methods(mock_item):
    mock_item._price = 10
    item = Item()
    assert item.total_price(2) == 20
