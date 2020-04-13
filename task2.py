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

