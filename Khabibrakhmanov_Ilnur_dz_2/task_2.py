"""
Необходимо  обработать список — обособить каждое целое число (вещественные не трогаем)
кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов. Подумать, какое условие записать,
чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
"""
original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for x in range(len(original_list)):
    original_list_part = str(original_list[x])   # переводим каждый объект списка в строку
    for c in range(len(original_list_part)):
        if original_list_part[0].isdigit():  # если первый объект строки цифра
            original_list_int = int(original_list_part)
            numb_1 = f'"{original_list_int:02d}"'
            original_list[x] = numb_1  # меняем объект [x] в списке на numb_1
        elif original_list_part[0] == '+' and len(original_list_part) > 1 and original_list_part[1].isdigit():
            # в противном случае, если первый объект списка '+', длина строки больше одного объекта
            # и второй объект строки цифра
            original_list_int = int(original_list_part)
            numb_2 = f'"{original_list_part[0]}{original_list_int:02d}"'
            original_list[x] = numb_2 # меняем объект [x] в списке на numb_2
        elif original_list_part[0] == '-' and len(original_list_part) > 1 and original_list_part[1].isdigit():
            # в противном случае, если первый объект списка '-', длина строки больше одного объекта
            # и второй объект строки цифра
            original_list_int = int(original_list_part)
            numb_3 = f'"{original_list_int:03d}"'
            original_list[x] = numb_3  # меняем объект [x] в списке на numb_3
temperature = ' '.join(original_list)  # соединяем список в одну строку
print(temperature)  # выводим результат
