#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Введите число n\n")
if number.isdigit():
    number = int(number)
    a = int((str(number) * 2))
    b = int((str(number) * 3))
    result = number + a + b
    print(result)