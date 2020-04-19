# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
#Решение 1
def my_func (x, y):
    try:
        z = x / y
        return z
    except ValueError:
        return "Ошибка ввода, это не число"
    except ZeroDivisionError:
        return "y не может быть равен 0"
    print(z)
print(my_func(int(input("Введите значение x = ")), int(input("Введите значение y = "))))

#Будет ли приемлим второй вариант решения? Потому что первый мне кажется кривым
#Решение 2
def my_func ():
    while True:
        a = input("Введите число: \n")
        if a.isdigit():
            a = int(a)
            break
        else:
            print("Ошибка ввода, это не число")

    while True:
        b = input("Введите еще одно число: \n")
        if b.isdigit():
            b = int(b)
            break
        else:
            print("Ошибка ввода, это не число")

    try:
        c = a/b
        return c

    except ZeroDivisionError:
        return "b не может быть равен 0"
print(my_func())