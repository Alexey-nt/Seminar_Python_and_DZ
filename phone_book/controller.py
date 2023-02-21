from operations import *
def get_data():
    last_name =    input('Введите Фамилию: ').strip()
    first_name =   input('Введите Имя: ').strip()
    middle_name =  input('Введите Отчество: ').strip()
    phone_number = input('Введите номер: ').strip()
    return (last_name, first_name, middle_name, phone_number)

def get_operation_number():
    operation = input().strip()
    while operation not in ('1','2','3','0'):
        print('Некорректный ввод, попробуйте еще раз:')
        operation = input().strip()
    return operation

def perform_operation(operation_number):
    if operation_number == '1': 
        print_all()
    elif operation_number == '2':
        add_an_entry(get_data())
    elif operation_number == '3':
        print('\n'.join(find_entry(input('Введите Фамилию, Имя, Отчество или Телефон: ').strip())))
    else:
        print('Завершение работы')

