# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии. 
# A = 3; B = 5 -> 243 (3⁵) 
# A = 2; B = 3 -> 8 
'''
def degree_of_number(x, y):
    if y > 0:
        return degree_of_number(x, y - 1) * x
    elif y < 0:
        return degree_of_number(x, y + 1) / x
    elif y == 0:
        return 1
    elif x == 0:
        return 0

a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
res = degree_of_number(a, b)
print(res)
'''
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы. 
# 2 2 
# 4
'''
def sum_digits(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return sum_digits(x + 1, y - 1)


a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
res = sum_digits(a, b)
print(res)
'''