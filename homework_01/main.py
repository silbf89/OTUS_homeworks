import re

FILENAME = 'contacts.txt'


def show_all():
    data = read_contacts_from_file()
    print(*data, sep='\n')


def find_contact():
    data = read_contacts_from_file()
    contacts = find_contacts_by_substring(data)
    print(*contacts, sep='\n')


def add_contact():
    new_contact = get_new_contact()
    with open(FILENAME, 'a', encoding='UTF-8') as f:
        f.write(new_contact + '\n')
    print('Контакт успешно добавлен')


def edit_contact():
    data = read_contacts_from_file()
    contacts = find_contacts_by_substring(data)
    contact = select_one_from_list(contacts)
    new_contact = get_new_contact()
    data.remove(contact)
    data.append(new_contact)
    with open(FILENAME, 'w', encoding='UTF-8') as f:
        for s in data:
            f.write(s + '\n')
    print('Контакт успешно изменён')


def delete_contact():
    data = read_contacts_from_file()
    contacts = find_contacts_by_substring(data)
    contact = select_one_from_list(contacts)
    data.remove(contact)
    with open(FILENAME, 'w', encoding='UTF-8') as f:
        for s in data:
            f.write(s + '\n')
    print('Контакт успешно удалён')


def read_contacts_from_file():
    with open(FILENAME, 'r', encoding='UTF-8') as f:
        data = [s.strip() for s in f]
    return data


def find_contacts_by_substring(data):
    search_string = re.split(r'[,\s]+', input('Введите данные для поиска контакта\n'))
    contacts = sorted(list(filter(lambda string: all([i.lower() in string.lower() for i in search_string]), data)))
    return contacts


def get_new_contact():
    while True:
        print('Введите данные в формате:\nФамилия, Имя, Отчество, ***-***-**-** (номер телефона), Место работы')
        contact = input()
        temp = contact.split(',')
        if len(temp) == 5 and len(temp[3]) == 14:
            return contact
        else:
            print('Данные введены в неверном формате\nПопробуйте еще раз')


def select_one_from_list(lst):
    if len(lst) == 1:
        return lst[0]
    print('По вашему запросу найдено несколько контактов, выберите один')
    for i in range(len(lst)):
        print(i, lst[i])
    index = int(input('Введите номер контакта: '))
    return lst[index]


command = {'1': show_all,
           '2': add_contact,
           '3': find_contact,
           '4': edit_contact,
           '5': delete_contact,
           }

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
