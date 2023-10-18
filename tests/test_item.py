from src.item import Item
import pytest


def test_item():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000


def test_instantiate_from_csv():
    item1 = Item.instantiate_from_csv("items.csv")
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number("100") == 100
    assert Item.string_to_number("100.0") == 100


def test_sum_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1 + item2 == 25
