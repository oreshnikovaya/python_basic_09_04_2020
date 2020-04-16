#2.Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_seconds = input("Введите время в секундах\n")
if time_in_seconds.isdigit():
    time_in_seconds = int(time_in_seconds)
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    result  = f'Время в формате чч:мм:сс: {hours}:{minutes}:{seconds}'
    print(result)


#Второй вариант:
while True:
    time = input("Введите время в секундах\n")
    if time.isdigit():
        time = int(time)
        break
    else:
        print("Ошибка ввода, это не число")
hh, mm, ss = time // 3600,(time % 3600) // 60, (time % 3600) % 60
print (f'{hh:>02}:{mm:>02}:{ss:>02}') #0 - вместо пробела, 2 - количество знаков
