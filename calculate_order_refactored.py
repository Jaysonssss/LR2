MIN_STUDENT_AGE = 18
PERCENT_BASE = 100
STANDARD_DELIVERY_CITIES = ("Москва", "Санкт-Петербург")
STANDARD_DELIVERY_FEE = 300
OTHER_DELIVERY_FEE = 500


def subtotal_after_discount(age, student, price, quantity, discount):
    subtotal = price * quantity
    if age >= MIN_STUDENT_AGE and student == True and discount > 0:
        subtotal = subtotal - subtotal * discount / PERCENT_BASE
    return subtotal


def delivery_fee(city):
    if city in STANDARD_DELIVERY_CITIES:
        return STANDARD_DELIVERY_FEE
    return OTHER_DELIVERY_FEE


def print_order(name, age, city, total):
    print("Заказ покупателя:", name)
    print("Возраст:", age)
    print("Город:", city)
    print("Итоговая стоимость:", total)


def calculate_order(name, age, student, price, quantity, discount, city):
    subtotal = subtotal_after_discount(age, student, price, quantity, discount)
    total = subtotal + delivery_fee(city)
    print_order(name, age, city, total)
    return total


def check_order(name, age, student, price, quantity, discount, city):
    """Возвращает сумму без доставки. Сигнатура сохранена для старых вызовов."""
    return subtotal_after_discount(age, student, price, quantity, discount)


def run_example():
    total = calculate_order(
        name="Иван",
        age=20,
        student=True,
        price=1000,
        quantity=3,
        discount=10,
        city="Москва",
    )
    print("Заказ обработан")
    return total


result = run_example()
