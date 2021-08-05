"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы
"""

names_of_workers = input('Введите имена сотрудников через запятую')
names_list = names_of_workers.split(', ')


def thesaurus(names_list):
    names = {
    }
    for x in range(len(names_list)):
        key_of_names = str(names_list[x][0]).capitalize()
        if key_of_names not in names:
            names[key_of_names] = list()
        if key_of_names in names:
            names[key_of_names].append(names_list[x])
    names_sorted = dict(sorted(names.items(), key=lambda x: x[0]))
    return names_sorted


print(thesaurus(names_list))
