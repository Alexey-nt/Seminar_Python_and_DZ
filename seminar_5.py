# Задача №31. Последовательностью Фибоначчи называется последовательность чисел 
# a0 , a1 , ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи 
# Задание необходимо решать через рекурсию
# Input: 7 
# Output: 21 
'''
def Fibonacci(n: int):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

n = int(input('Введите номер числа Фибоначчи: '))
# for i in range(n):
#     num_fib = Fibonacci(i)
#     print(i + 1, '-', num_fib)

print(n, 'число Фибоначчи - ', Fibonacci(n - 1))
'''

# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1
'''
evaluation = [int(x) for x in input().split()]

def min_replace_max(list1: list):
    max1 = max(list1)
    min1 = min(list1)
    for i in list1:
        if list1[i] == max1:
            list1[i] = min1

min_replace_max(evaluation)
print(evaluation)
'''
# Решение №2
'''
from random import randint

my_list = [randint(1, 5) for _ in range(randint(3, 7))] # Создание списка случайных чисел от 3 до 7 со значениями от 1 до 5
print(my_list)
max_elem = max(my_list) # встроенная функция поиска max элемента
min_elem = min(my_list) # встроенная функция поиска min элемента

for i in range(len(my_list)):
    if my_list[i] == max_elem:
        my_list[i] = min_elem

print(my_list)
'''

# Задача №35. Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым 
# Напоминание: 
# Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
# Input: 5 Output: yes
'''
def simple_num(x):
    for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
        return 'no'
    return 'yes'

n = int(input('Введите число: '))
print(simple_num(n))
'''
# Решение № 2
'''
def prime(n):
    i = 2
    flag = True
    while i < n and flag:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return 'yes'
    return 'no'

n = int(input())
print(prime(n))
'''
# Задача №37. Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). 
# Input:    2 -> 3 4 
# Output: 4 3
'''
n = int(input('Введите число: '))

num_lst = [i for i in range(1, n + 1)]
print(num_lst)
'''
# Решение № 2
'''
from random import randint
def recurs(x):
    if x == 0:
        print()
        return
    number = randint(0, 100)
    print(number, end=' ')
    recurs(x - 1)
    print(number, end=' ')
    
n = 6
recurs(n)
'''
# Решение № 3
'''
def print_numbers(n):
    if n > 0:
        numb = int(input('Введите число: '))
        print_numbers(n-1)
        print(numb, end=' ')
    else:
        print('Числа в обратном порядке')

N = int(input())
print_numbers(N)
'''