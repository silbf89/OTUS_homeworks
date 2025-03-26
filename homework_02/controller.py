from model import Contact, ContactBook
import view
import re

FILENAME = 'contacts.txt'

contact_book = ContactBook(FILENAME)


def show_all():
    view.show_data(sorted(contact_book.contacts))


def find_contact():
    contacts = find_contacts_by_query(contact_book.contacts)
    if len(contacts) > 0:
        view.show_data(sorted(contacts))
    else:
        view.show_data('Контакты не найдены')


def add_contact():
    new_contact = get_new_contact()
    contact_book.add_contact(new_contact)
    view.show_data('Контакт успешно добавлен')


def edit_contact():
    contacts = find_contacts_by_query(contact_book.contacts)
    if len(contacts) > 1:
        old_contact = contacts[view.select_one(contacts)]
    elif len(contacts) == 1:
        old_contact = contacts[0]
    else:
        view.show_data('Контакты не найдены')
        return
    view.show_data(old_contact)
    new_contact = get_new_contact()
    contact_book.edit_contact(old_contact, new_contact)
    view.show_data('Контакт успешно изменён')


def delete_contact():
    contacts = find_contacts_by_query(contact_book.contacts)
    if len(contacts) > 1:
        old_contact = contacts[view.select_one(contacts)]
    else:
        old_contact = contacts[0]
    view.show_data(old_contact)
    contact_book.delete_contact(old_contact)
    view.show_data('Контакт успешно удалён')


def find_contacts_by_query(all_contacts: list[Contact]):
    search_words = re.split(r'[,\s]+', view.get_search_query())
    return list(filter(lambda contact: search_words in contact, all_contacts))


def get_new_contact():
    has_all_data = False
    new_contact = None

    while not has_all_data:
        data = view.get_contact_data(['фамилия', 'имя', 'номер телефона'], True)
        try:
            new_contact = Contact(data['фамилия'], data['имя'], data['номер телефона'])
        except ValueError as ex:
            view.show_data(ex)
            continue

        while not has_all_data:
            data = view.get_contact_data(['отчество', 'место работы', 'комментарий'], False)
            try:
                new_contact.patronymic = data['отчество']
                has_all_data = True
            except ValueError as ex:
                view.show_data(ex)
                continue

        new_contact.job = data['место работы']
        new_contact.comment = data['комментарий']

    return new_contact
