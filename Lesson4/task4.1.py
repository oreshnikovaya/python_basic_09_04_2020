# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

_, time, salary, bonus = argv
try:
    # time = int(time)
    # salary = int(salary)
    # bonus = int(bonus)
    # res = time * salary + bonus
    res = float(time) * float(salary) + float(bonus)
    print(f'Заработная плата сотрудника  {res}')
except ValueError as e:
    print('Это не число')
    print(e)
