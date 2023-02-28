import os
os.system('cls')

def record_phonebook_data(): # запись
    name = input('Введите имя: \n')
    patronymic = input('Введите отчество: \n')
    surname = input('Введите фамилию: \n')
    number = input('Введите номер телефона: \n')
    record = [name, ' ', patronymic, ' ', surname, ' ', number]
    try:
        with open('phonebook.txt', 'a+', encoding='utf-8') as file:
            file.writelines(record)
            file.writelines('\n')
    except:
        print('Ошибка работы с файлом.')

def read_phonebook_data(): # чтение
    try:
        with open('phonebook.txt', 'r+', encoding='utf-8') as file:
            s = file.readlines()
            return s
    except:
        print('Ошибка чтения.')

def changes_phonebook_data(data): # внесение изменений
    changes_phonebook = []
    print('Введите новые имя, фамилию или отчество\n'
          'для удаления записи оставьте пробел')
    name = input('Выберите для изменения имя: \n')
    patronymic = input('Выберите для изменения отчество: \n')
    surname = input('Выберите для изменения фамилию: \n')
    number = input('Введите телефон: \n')
    changes_vol = (f'{name}' ' ' f'{patronymic}' ' ' f'{surname}' ' ' f'{number}')
    try:
        with open('phonebook.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                changes_phonebook.append(line)
    except:
        print('Ошибка чтения.')

    for i in range(len(changes_phonebook)):
        if changes_phonebook[i] == changes_phonebook[data]:
            changes_phonebook[i] = f'{changes_vol}\n'
    try:
        with open('phonebook.txt', 'w', encoding='utf-8') as file:
            file.writelines(changes_phonebook)
            file.writelines('\n')
    except:
        print('Ошибка чтения.')