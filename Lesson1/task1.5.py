#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = input("Введите значение выручки:\n")
costs = input("Введите значение издержек фирмы:\n")
if proceeds.isdigit():
    proceeds = int(proceeds)
elif costs.isdigit():
    costs = int(costs)
if int(str(proceeds)) > int(str(costs)):
    profit = int(str(proceeds))-int(str(costs))
    rent = int(str(profit))/int(str(proceeds))
    print (f"Отличная работа. У вас есть прибыль {profit} и рентабельность выручки {rent}")
    staff = (input("Сколько сотрудников работает в фирме:\n"))
    if staff.isdigit():
        staff = int(staff)
        print(f"Прибыль фирмы в расчете на одного сотрудника {profit / staff}")
if int(str(costs)) > int(str(proceeds)):
    loss = int(str(costs)) - int(str(proceeds))
    print(f"Плохая работа. У вас есть убыток {loss} ")