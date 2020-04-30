# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
my_list = ['Hello world\n', 'Chao\n', 'Hola\n']
with open("test_1.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
lines = 0
for line in open("test_1.txt").readlines():
    lines += 1
    print(f"Номер строки {lines}")
    line = line.split(' ')
    print(f"Слова в строке {line}")
    words = len(line)
    print(f"Количество слов в строке {words}")

