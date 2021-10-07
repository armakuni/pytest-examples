from unittest import mock


class Item():
    def price(self):
        pass


@mock.patch.object(Item, 'price', return_value=5)
def test_mocking_object_method_with_return_value(mock_price):
    item = Item()
    assert item.price() == 5


@mock.patch.object(Item, 'price')
def test_mocking_object_method(mock_price):
    mock_price.return_value = 5
    item = Item()
    assert item.price() == 5
