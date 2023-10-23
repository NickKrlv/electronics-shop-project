import csv
import os
from csv import DictReader


class InstantiateCSVError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    InstantiateCSVError = None
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return NotImplemented

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, csv_filename='items.csv'):
        """
        Инициализирует экземпляры класса `Item` данными из файла items.csv.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, csv_filename)
        try:
            with open(csv_path, 'r', encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if 'name' in row and 'price' in row and 'quantity' in row:
                        name = row['name']
                        price = cls.string_to_number(row['price'])
                        quantity = cls.string_to_number(row['quantity'])
                        cls.all.append(cls(name, price, quantity))

                    else:
                        raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Преобразует строковое значение в целое число.
        """
        return int(float(value))
