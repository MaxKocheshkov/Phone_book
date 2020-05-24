from Phone_contact import Contact

if __name__ == '__main__':
    user_name = input('Введите имя: ')
    user_surname = input('Введите фамилию: ')
    user_phone = int(input('Введите номер телефона: '))
    user_selected = input('Добавить в избранное? да/нет: ')
    user_additionally_1 = input('Введите ссылку на телеграмм: ')
    user_additionally_2 = input('Введите email: ')
    if user_selected == 'да':
        Contact.selected_contact = True
    else:
        Contact.selected_contact = False

    user_input_data = Contact(user_name, user_surname, user_phone, user_selected, telegram=user_additionally_1,
                              email=user_additionally_2)
    print(user_input_data)