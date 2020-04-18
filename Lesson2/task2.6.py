#6.*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# goods = int(input("Введите количество товара:\n "))
# n = 1
# my_dict = []
# my_list = []
# my_analys = {}
# while n <= goods:
#     my_dict = dict({"название": input("Введите название:\n "), "цена": input("Введите цену:\n "),
#                     "количество": input("Введите количество:\n "), "eд": input("Введите единицу измерения:\n ")})
#     my_list.append((n, my_dict))
#     n += 1
#     my_analys = dict(
#         {"название": my_dict.get("название"),
#          "цена": my_dict.get("цена"),
#          "количество": my_dict.get("количество"),
#          "ед": my_dict.get("ед")})
# print(my_list)
# print(my_analys)

#Второй способ

product_template = {
    'название': ("имя товара", str),
    'цена': ("стоимость товара", int),
    'количество': ("количество товара", int),
    'ед': ("Единицы имзмерения (шт,кг и тд)", str),
}

#Спрашиваем, хочет ли юзер добавить еще товар в корзину.
# В Случае, если нет, то цикл while next_enter прекратится
next_enter = True

auto_inc = 1 #номер в кортеже
products_list = []

while next_enter:
    #словарь, в который мы будем добавлять атрибуты товара
    product = {}
    #заполняем товар по шаблону
    for key, value in product_template.items():
        #цикл while True используется для того, чтобы переспросить вопрос, если будет неверный ввод по типу
        while True:
            user_value = input(f'{value[0]}\n') #текст вопроса берем из product_template
            try:
                user_value = value[1](user_value) #str (user_value)
            except ValueError as e:
                print(f"{e}\nНеверное значение данных")
                continue
            product[key] = user_value
            break
    products_list.append((auto_inc, product))
    auto_inc += 1

    # тут мы проверим надо еще товар вводить или нет
    while True:
        next_add = input ("Добавить еще продукт? Да/Нет \n")
        if next_add.lower() in ("да", "нет"):
            next_enter = next_add.lower() == "да"
            break
        else:
            print("Неверный ввод, повторите")

print(products_list)

products_analytics= {}
#собиарем словарь аналитики
for key in product_template:
    result = []
    for itm in products_list:
        result.append(itm[1][key])
    products_analytics[key] = result

print(products_analytics)
