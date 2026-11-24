def calculate_order(name, age, student, price, quantity, discount, city):
    total = price * quantity

    if age >= 18 and student == True:
        if discount > 0:
            total = total - total * discount / 100

    if city == "Москва":
        total = total + 300
    elif city == "Санкт-Петербург":
        total = total + 300
    else:
        total = total + 500

    print("Заказ покупателя:", name)
    print("Возраст:", age)
    print("Город:", city)
    print("Итоговая стоимость:", total)

    return total

def check_order(name, age, student, price, quantity, discount, city):
    total = price * quantity

    if age >= 18 and student == True:
        if discount > 0:
            total = total - total * discount / 100

    return total

price = 1000
quantity = 3
discount = 10
city = "Москва"

result = calculate_order(
    "Иван",
    20,
    True,
    price,
    quantity,
    discount,
    city
)

print("Заказ обработан")