from unittest import mock


def test_spy_on_function():
    with mock.patch('test_spying.foo', wraps=foo) as foo_spy:
        assert foo(4) == 8
        foo_spy.assert_called_once()


def foo(input):
    return input * 2


class Item():
    def price(self):
        return 4


def test_spy_on_object_method():
    item = Item()
    with mock.patch.object(item, 'price', wraps=item.price) as item_price_spy:
        assert item.price() == 4
        item_price_spy.assert_called_once()
