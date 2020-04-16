#Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
#https://taskcode.ru/cycles/max-digit

# a = input("Введите число:\n") # a - заданноче число, m - максимальная цифра.
# if a.isdigit():
#     a = int(a)
# a = a // 10
# while a > 0:
#     if a % 10 > m:
#         m = a % 10
#     a = a // 10
# print(m)

#Второй вариант
while True:
    user_num = input("Введите целое число\n")
    if user_num.isdigit():
        user_num = int(user_num)
        break
    else:
        print("Ошибка ввода, это не число")

result = 0
while user_num and result != 9:
    tmp = user_num % 10
    if tmp > result:
        result = tmp
    user_num //= 10

print (result)



