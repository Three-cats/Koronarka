"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
"""
num_on_en = input('Введите число от 0 до 10 со строчной буквы на английском языке')


def num_translate():
    num_on_rus = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    for item in num_on_rus:
        if item == num_on_en:
            return num_on_rus[item]


print(num_translate())
