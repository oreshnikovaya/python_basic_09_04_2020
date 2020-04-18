#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_string = input("Введите несколько слов:\n")
my_list = []
number = 1
for i in range(my_string.count(' ') + 1 ):
    my_list = my_string.split()
    if len(str(my_string)) <= 10:
        print (f'{number} {my_list[i]}')
        number += 1
    else:
        print (f'{number} {my_list[i] [0:10]}')
        number += 1

#Второй способ

user_words = input()

for idx, word in enumerate(user_words.split(' '), 1):
    print(f'{idx}: {word[:10]}')