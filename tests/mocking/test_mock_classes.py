from unittest import mock


class Item():
    def price(self):
        return 4


@mock.patch.object(Item, 'price', return_value=5)
def test_mocking_object_method_with_return_value(mock_price):
    item = Item()
    assert item.price() == 5


def test_mocking_object_method():
    item = Item()
    with mock.patch.object(item, 'price', return_value=5):
        assert item.price() == 5
    assert item.price() == 4
