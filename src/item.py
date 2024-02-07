import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return f"{self.__name}"

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price = self.quantity * self.price
        return all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price - self.price * self.pay_rate

    @name.setter
    def name(self, value):
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls, file_name):
        cls.all.clear()
        with open(file_name, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                name = item['name']
                price = cls.string_to_number(item['price'])
                quantity = int(item['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number):
        return int(float(number))

