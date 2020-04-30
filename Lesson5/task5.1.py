# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
file_name = input('Файл: ')
my_file = open(file_name,'w')
while True:
    line = input('Введите текст: \n')
    if line == '':
        break
    my_file.write(line + '\n')
my_file.close()