import pytest
from src.InstantiateCSVError import InstantiateCSVError
from src.item import Item


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv("csv_filename='items.txt")


def test_instantiate_csv_error():
    with pytest.raises(InstantiateCSVError) as exc_info:
        error_instance = InstantiateCSVError('non_existent.csv')  # Передайте несуществующий файл

    assert str(exc_info.value) == "Файл item.csv поврежден"
