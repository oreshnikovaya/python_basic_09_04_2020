# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

my_list = [1, 2, 2, 3, 4, 1, 2]
print(f'Новый список: {[i for i in my_list if my_list.count(i)==1]}')