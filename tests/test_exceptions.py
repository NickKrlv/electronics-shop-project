import pytest
from src.item import InstantiateCSVError
from src.item import Item


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv(csv_filename='items.txt')


def test_instantiate_from_csv_corrupted_file():
    with pytest.raises(Item.InstantiateCSVError, match="Файл item.csv поврежден"):
        Item.instantiate_from_csv(csv_filename='items_2.txt')
