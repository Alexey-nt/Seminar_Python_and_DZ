from function_module import record_phonebook_data, read_phonebook_data, changes_phonebook_data

def operation_function(data): # инициирует функцию записи
    if data == 1:
        return record_phonebook_data()
    elif data == 2:
        search_vol = input(
            'для поиска введите Имя, Фамилию или Отчество: ')
        print('*'*10)
        for i in range(len(read_phonebook_data())):  # инициирует функцию чтения
            if search_vol in read_phonebook_data()[i]:
                print(read_phonebook_data()[i])
        else:
            return (f'{search_vol} - нет в списке.')
    elif data == 3:
        changes_vol = input(
            'для изменения введите Имя, Фамилию или Отчество: ')
        print('*'*10)
        for i in range(len(read_phonebook_data())):
            if changes_vol in read_phonebook_data()[i]:
                print(f'{i} => {read_phonebook_data()[i]}')

        changes_vol = int(input('Введите номер записи для изменения: \n' # инициирует функцию внесения изменений
                                '******************\n'
                                '==> '))
        changes_phonebook_data(changes_vol)
    else:
        print('До Встречи.')