from controller import operation_function
import os
os.system('cls')

def dialog_values():
    incoming_vol = int(input(
        'Выберите:\n'
        '1 - для создания записи\n'
        '2 - для поиска информации\n'
        '3 - для внесения изменений\n'
        '4 - для выхода\n'
        '***************************\n'
        '==> '))
    while incoming_vol < 4:
        if incoming_vol == 1:
            return incoming_vol
        elif incoming_vol == 2:
            return incoming_vol
        elif incoming_vol == 3:
            return incoming_vol
        else:
            print('Ошибка ввода!')
            return dialog_values()
        
operation_function(dialog_values())

