from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(csv_filename='items.txt')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(csv_filename='items_2.txt')
    # InstantiateCSVError: Файл item.csv поврежден
