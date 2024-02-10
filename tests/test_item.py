import pytest

from src.item import Item


@pytest.fixture
def position():
    return Item("Смартфон", 100, 1)


def test_item_init(position):
    assert position.name == "Смартфон"
    assert position.price == 100
    assert position.quantity == 1


def test_calculate_total_price():
    item = Item('Смартфон', 20000, 100)
    assert item.calculate_total_price() == 2000000


def test_apply_discount():
    item = Item('Смартфон', 2000, 3)
    Item.pay_rate = 0.1

    item.apply_discount()

    assert item.price == 1800.0


def test_name_setter():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'


def test_name_setter_truncate():
    item = Item('Телефон', 25000, 3)
    item.name = 'Суперсмартфон'
    assert item.name == 'Суперсмартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_str(position):
    item = Item('Смартфон', 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"
    assert str(item) == 'Смартфон'


def test_add(position, phone1):
    """
    Тест метода add
    """

    assert position + phone1 == 11
