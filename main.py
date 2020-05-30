from Phone_contact import Contact
from Phone_book import PhoneBook


user_book_name = input('Введите название телефонной книги: ')
user_book = PhoneBook(user_book_name)


def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'i':  # Ввод данных контакта
            user_name = input('Введите имя: ')
            user_surname = input('Введите фамилию: ')
            user_phone = int(input('Введите номер телефона: '))
            user_selected = input('Добавить в избранное? да/нет: ')
            user_additionally_1 = input('Введите ссылку на телеграмм: ')
            user_additionally_2 = input('Введите email: ')
            user_record = input('Введите номер записи: ')
            if user_selected == 'да':
                Contact.selected_contact = True
            else:
                Contact.selected_contact = False
            user_input_data = Contact(user_name, user_surname, user_phone, user_selected, telegram=user_additionally_1,
                                      email=user_additionally_2)
        elif user_input == 'a':  # Добавление контакта
            user_book.add_contact('Имя', user_input_data.name)
            user_book.add_contact('Фамилия', user_input_data.surname)
            user_book.add_contact('Телефон', user_input_data.phone_number)
            user_book.add_contact('В избранных', user_input_data.selected_contact)
            user_book.add_contact('Дополнительная информация', str(user_input_data.additionally))
        elif user_input == 'w':  # Запись в книгу
            user_book.write_in_book(user_record)
        elif user_input == 'c':  # Вывод книги
            print(user_book.conclusion())
        elif user_input == 'd':  # Удаление контакта из книги
            print(user_book.del_for_number())
        elif user_input == 's':  # Вывод избранных
            print(user_book.selected_phone())
        elif user_input == 'f':  # Поиск по имени и фамилии
            print(user_book.name_search())
        elif user_input == 'q':  # Выход
            print('До свидания!')
            break


if __name__ == '__main__':
    main()
