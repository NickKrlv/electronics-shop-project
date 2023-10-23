import csv
import os


class InstantiateCSVError(Exception):
    correct_items_csv = [{'name': 'Смартфон', 'price': '100', 'quantity': '1'},
                         {'name': 'Ноутбук', 'price': '1000', 'quantity': '3'},
                         {'name': 'Кабель', 'price': '10', 'quantity': '5'},
                         {'name': 'Мышка', 'price': '50', 'quantity': '5'},
                         {'name': 'Клавиатура', 'price': '75', 'quantity': '5'}]

    def __init__(self, csv_filename='items.csv'):
        self.csv_filename = csv_filename
        self.fact_items_csv = []

        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, csv_filename)

        try:
            with open(csv_path, 'r', encoding='windows-1251') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    self.fact_items_csv.append({'name': row['name'], 'price': row['price'], 'quantity': row['quantity']})

        except Exception as e:
            super().__init__(f"Файл item.csv поврежден")





