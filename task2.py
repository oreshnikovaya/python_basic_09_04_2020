#Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

#Решение только для четного количества элементов. Можно ли как-то это доделать, чтобы с нечетынм количеством
#нарезку списка можно было использовать?
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = l[:]
n[::2], n[1::2] = n[1::2], n[::2]
print(n)

#Не очень понятно, как сделать так, чтобы не нагружать input intом
my_list_1 = []
for i in range(int(input("Введите количество элементов в списке:\n"))):
    my_list_1.append(int(input("Введите элемент списка:\n")))
j = 0
for i in range(int(len(my_list_1) / 2)):
    my_list_1[j], my_list_1[j + 1] = my_list_1[j + 1], my_list_1[j]
    j += 2
print(my_list_1)




