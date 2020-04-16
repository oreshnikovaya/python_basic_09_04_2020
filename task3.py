#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Введите число n\n")
a = number * 2
b = number * 3
result = int(number) + int(a) + int(b)
print(result)