"""
Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из двух случайных слов, взятых из трёх списков
"""
import random

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

for n  in range(0,5):
    def get_jokes():
        from random import choice

        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        return joke
    print(get_jokes())


