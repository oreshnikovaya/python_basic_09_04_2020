#6.*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

goods = int(input("Введите количество товара:\n "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= goods:
    my_dict = dict({"название": input("Введите название:\n "), "цена": input("Введите цену:\n "),
                    "количество": input("Введите количество:\n "), "eд": input("Введите единицу измерения:\n ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {"название": my_dict.get("название"),
         "цена": my_dict.get("цена"),
         "количество": my_dict.get("количество"),
         "ед": my_dict.get("ед")})
print(my_list)
print(my_analys)