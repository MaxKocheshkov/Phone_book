from Phone_contact import Contact

book_dict = {}

class PhoneBook:

    def __init__(self, name_book):
        self.name_book = name_book
        self.contacts = {}

    def add_contact(self, name: str, contact: Contact):
        self.contacts[name] = contact
        return self.contacts

    def write_in_book(self, record_number):
        self.record_number = record_number
        book_dict.update({
            self.record_number: list(self.contacts.values())
                        })

    def conclusion(self):
        return f'{self.name_book}: {book_dict}'

    def del_for_number(self):
        user_del_number = int(input('Введите номер для удаления: '))
        for number, record in book_dict.items():
            if user_del_number in record:
                book_dict.pop(number)
                return f'{self.name_book}: {book_dict}'

    def selected_phone(self):
        for selected_record in book_dict.values():
            if 'да' in selected_record:
                return selected_record

    def name_search(self):
        user_search_name = input('Введите имя для поиска: ')
        user_search_surname = input('Введите фамилию для поиска: ')
        for find_name in book_dict.values():
            if user_search_name in find_name and user_search_surname in find_name:
                return find_name




