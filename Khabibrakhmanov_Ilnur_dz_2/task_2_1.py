original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for x in range(len(original_list)):
    original_list_part = str(original_list[x])
    if original_list_part[0].isdigit():
        original_list.insert(x + 1, '"')
for x in range(len(original_list)):
    original_list_part = str(original_list[x])
    if original_list_part[0] == '+' and len(original_list_part) > 1 and original_list_part[1].isdigit():
        original_list.insert(x + 1, '"')
for x in range(1, len(original_list), 2):
    original_list_part = str(original_list[x])   # переводим каждый объект списка в строку
    if original_list_part[0].isdigit():
        original_list.insert(x, '"')
for x in range(len(original_list)):
    original_list_part = str(original_list[x])
    if original_list_part[0] == '+' and len(original_list_part) > 1 and original_list_part[1].isdigit():
        original_list.insert(x, '"')
        break
print(original_list)

for x in range(len(original_list)):
    original_list_part = str(original_list[x])
    if original_list_part[0].isdigit():  # если первый объект строки цифра
        original_list_int = int(original_list_part)
        numb_1 = f'{original_list_int:02d}'
        original_list[x] = numb_1  # меняем объект [x] в списке на numb_1
    elif original_list_part[0] == '+' and len(original_list_part) > 1 and original_list_part[1].isdigit():
        original_list_int = int(original_list_part)
        numb_2 = f'{original_list_part[0]}{original_list_int:02d}'
        original_list[x] = numb_2 # меняем объект [x] в списке на numb_2
    elif original_list_part[0] == '-' and len(original_list_part) > 1 and original_list_part[1].isdigit():
        original_list_int = int(original_list_part)
        numb_3 = f'{original_list_int:03d}'
        original_list[x] = numb_3  # меняем объект [x] в списке на numb_3
temperature = ' '.join(original_list)  # соединяем список в одну строку
for x in range(len(temperature)):
    if temperature[x] == '"' and temperature[x+1].isdigit():
        string = 'temperature[x]  temperature[x+1]'
        temperature = ' '.join(temperature.split())
print(temperature)  # выводим результат