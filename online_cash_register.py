import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {
            'чипсы': 50,
            'кола': 100,
            'печенье': 45,
            'молоко': 55,
            'кефир': 70,
        }
        self.__tax_rate = {
            'чипсы': 20,
            'кола': 20,
            'печенье': 20,
            'молоко': 10,
            'кефир': 10,
        }

    # 1. геттер name_items
    @property
    def name_items(self):
        return self.__name_items

    # 1. геттер number_items
    @property
    def number_items(self):
        return self.__number_items

    # 2. add_item_to_cheque - добавить товар в чек.
    def add_item_to_cheque(self, name: str) -> None:
        # Проверка длины названия товара
        if len(name) == 0 or len(name) > 40:
            raise ValueError(
                'Нельзя добавить товар, если в его названии нет символа или их больше 40'
            )

        # Проверка наличия товара в справочнике
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарнои справочнике')

        # Добавление товара в чек
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. delete_item_from_check - удалить товар из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')

        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. check_amount - посчитать общую сумму покупок
    def check_amount(self) -> float:
        total = []

        for item in self.__name_items:
            total.append(self.__item_price[item])

        subtotal = sum(total)

        if self.__number_items > 10:
            return 0.9 * subtotal
        return subtotal

    # 5. twenty_percent_tax_calculation - вычислить НДС для товаров
    #    со ставкой 20%
    def twenty_percent_tax_calculation(self) -> float:
        # Список товаров со ставкой 20%
        twenty_percent_tax: list[str] = []

        # Список цен этих товаров
        total: list[float] = []

        # Отбираем товары из чека с налоговой ставкой 20%
        for name in self.__name_items:
            if self.__tax_rate.get(name) == 20:
                twenty_percent_tax.append(name)
                total.append(self.__item_price[name])

        # Общая стоимость товаров со ставкой 20%
        subtotal = sum(total)

        # Скидка 10% если в чеке более 10 товаров
        if self.__number_items > 10:
            discount_rate = 0.10
            subtotal = subtotal * (1 - discount_rate)

        # НДС 20%
        vat = 0.2 * subtotal

        return vat

    # 6. ten_percent_tax_calculation - вычислить НДС для товаров
    #    со ставкой 10%
    def ten_percent_tax_calculation(self) -> float:
        # Список товаров со ставкой 10%
        ten_percent_tax: list[str] = []

        # Список цен этих товаров
        total: list[float] = []

        # Отбираем товары из чека с налоговой ставкой 10%
        for name in self.__name_items:
            if self.__tax_rate.get(name) == 10:
                ten_percent_tax.append(name)
                total.append(self.__item_price[name])

        # Общая стоимость товаров со ставкой 10%
        subtotal = sum(total)

        # Скидка 10% если в чеке более 10 товаров
        if self.__number_items > 10:
            discount_rate = 0.10
            subtotal = subtotal * (1 - discount_rate)

        # НДС 10%
        vat = 0.1 * subtotal

        return vat

    # 7. total_tax - посчитать общую сумму налогов
    def total_tax(self) -> float:
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    # 8. get_telephone_number - вернуть номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')

        if len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')

        return f'+7{telephone_number}'

    # Доп. get_date_and_time - вернуть дату и время покупки
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()

        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year],
        ]

        for name, getter in date:
            value = getter(now)
            date_and_time.append(f'{name}: {value}')

        return date_and_time

