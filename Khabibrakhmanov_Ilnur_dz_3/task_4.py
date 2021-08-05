dates_of_workers = input('Введите имя и фамилию сотрудников через запятую: ')
dates_list = dates_of_workers.split(', ')


def thesaurus(dates_list):
    surnames = {
    }

    for x in range(len(dates_list)):
        key_of_surnames = str(dates_list[x].split()[-1][0]).capitalize()
        key_of_names = str(dates_list[x].split()[0][0]).capitalize()

        names = {}
        if key_of_surnames not in surnames:
            # names = {}
            surnames[key_of_surnames] = names
        if key_of_surnames in surnames:
            if key_of_names not in names:
                names[key_of_names] = list()
            if key_of_names in names:
                names[key_of_names].append(dates_list[x])
    return surnames


print(thesaurus(dates_list))
