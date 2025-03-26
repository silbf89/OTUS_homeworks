import controller


command = {'1': controller.show_all,
           '2': controller.add_contact,
           '3': controller.find_contact,
           '4': controller.edit_contact,
           '5': controller.delete_contact,
           }


def show_menu():
    while True:
        print('Доступные действия:\n'
              '1. Показать все контакты,\n'
              '2. Создать контакт,\n'
              '3. Найти контакт,\n'
              '4. Изменить контакт,\n'
              '5. Удалить контакт, \n'
              '6. Выход')
        cmd = input('Выберите номер действия\n')
        if cmd in '12345':
            command[cmd]()
        elif cmd == '6':
            break
        else:
            print('Неверная команда, попробуйте снова')


def show_data(data):
    if isinstance(data, list):
        print(*[str(item) for item in data], sep='\n')
    else:
        print(str(data))


def select_one(lst: list):
    print('Найдено несколько контактов, выберите один:')
    for i in range(len(lst)):
        print(i, str(lst[i]))
    return int(input('Введите номер контакта: '))


def get_search_query():
    return input('Введите данные для поиска контакта: ')


def get_contact_data(lst: list, required: bool):
    data = {}

    if required:
        print('Введите обязательные данные')
    else:
        print('Введите дополнительные данные (можете оставить строку пустой, если данные отсутствуют)')

    for item in lst:
        data[item] = input(f'{item.capitalize()}: ')

    return data

show_menu()
