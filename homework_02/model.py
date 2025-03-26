class Contact:
    def __init__(self, surname, name, phone_number, patronymic='', job='', comment=''):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number
        self.job = job
        self.comment = comment

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str) and surname.isalpha():
            self._surname = surname.lower().capitalize()
        else:
            raise ValueError('Некорректная фамилия')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name.lower().capitalize()
        else:
            raise ValueError('Некорректное имя')

    @property
    def patronymic(self):
        return self._patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if patronymic != '':
            if isinstance(patronymic, str) and patronymic.isalpha():
                self._patronymic = patronymic.lower().capitalize()
            else:
                raise ValueError('Некорректное отчество')
        else:
            self._patronymic = patronymic

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if isinstance(phone_number, str) and phone_number.isdigit():
            self._phone_number = phone_number
        else:
            raise ValueError('Некорректный номер телефона')

    def __str__(self): # переопределяем метод str для перевода объектов типа Class в string
        return (f'{self.surname}, '
                f'{self.name}, '
                f'{self.patronymic if self.patronymic != "" else "-"}, '
                f'{self.phone_number}, '
                f'{self.job if self.job != "" else "-"}, '
                f'{self.comment if self.comment != "" else "-"}')

    def __lt__(self, other): # переопределяем оператор '<' для сравнения объектов типа Class
        return str(self) < str(other)

    def __contains__(self, list_of_str): # переопределяем оператор 'in' для работы с объектами типа Class
        return all([string.lower() in str(self).lower() for string in list_of_str])

    @staticmethod
    def from_string(string: str): # метод меняющий тип объекта со string на Class
        values = string.split(', ')
        return Contact(values[0],
                       values[1],
                       values[3],
                       values[2] if values[2] != '-' else '',
                       values[4] if values[4] != '-' else '',
                       values[5] if values[5] != '-' else '',)


class ContactBook:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r', encoding='UTF-8') as f:
            self.contacts = [Contact.from_string(line.strip()) for line in f.readlines()]

    def save_changes(self):
        with open(self.filename, 'w', encoding='UTF-8') as f:
            for contact in self.contacts:
                f.write(str(contact) + '\n')

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_changes()

    def delete_contact(self, contact):
        self.contacts.remove(contact)
        self.save_changes()

    def edit_contact(self, old_contact, new_contact):
        self.contacts.remove(old_contact)
        self.contacts.append(new_contact)
        self.save_changes()
