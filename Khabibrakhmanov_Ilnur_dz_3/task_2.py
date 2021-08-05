"""
Доработать предыдущую функцию num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы.
"""

num_on_en = input('Введите число от 0 до 10  на английском языке')


def num_translate_adv():
    num_on_en_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    num_on_rus = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    for num_en, num_rus in zip(num_on_en_list, num_on_rus):
        if num_en == num_on_en:
            return num_rus
        if num_en.capitalize() == num_on_en:
            return num_rus.capitalize()


print(num_translate_adv())
