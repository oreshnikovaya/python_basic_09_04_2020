# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count
from itertools import cycle

def my_count_func(start_number, stop_number):
    for i in count(start_number):
        if i > stop_number:
            break
        else:
            print(i)
def my_cycle_func(my_list, iteration):
    j = 0
    iter = cycle(my_list)
    while j < iteration:
        print(next(iter))
        j+=1
my_count_func(start_number = int(input("Введите первый номер:\n")),
              stop_number = int(input("Введите последний номер:\n")))
my_cycle_func(my_list = [3, 4], iteration = int(input("Введите количество итераицй:\n")))