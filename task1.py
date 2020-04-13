# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

var_int = 2
var_float=10.0
var_bool=True
var_str = "Sonya"
var_none = None
print(var_int,var_float, var_bool, var_str, var_none)

day_of_the_week = input("Какой сегодня день недели?\n")
date = input("Какое сегодня число?\n")
if date.isdigit():
    date = int(date)
    result = f'Сегодня {day_of_the_week}, {date} число'
    print(result)