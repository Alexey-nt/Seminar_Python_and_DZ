# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0 
# 2
'''
count = int(input('Введите кол-во монет: '))
side_0 = 0
side_1 = 0
for i in range(1, count + 1):
    side = int(input('Введите сторону монеты, где 0 -> решка, 1 -> орел: '))
    if side == 0:
        side_0 += 1
    elif side == 1:
        side_1 += 1


if side_0 == side_1:
    print(f'Несоответствие между монетами одинаковое, можно выбрать любую сторону для переворачивания. Кол-во переворачиваний {int(count / 2)}')
elif side_0 == count or side_1 == count:
    print('Вам нечего переворачивать.')

side_min = 0
if side_0 < side_1:
    side_min = side_0
elif side_1 < side_0:
    side_min = side_1

print(f'Минимальное кол-во для переворачивания: {side_min}')
'''

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа. 

# S=4 P=4 -> x=2 y=2
# S=5 P=6 -> x=2 y=3 

s = int(input('Введите число, обозначающее сумму загаданных чисел: '))
p = int(input('Введите число, обозначающее произведение загаданных чисел: '))


'''
discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")
'''



# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N. 

# 10 -> 1 2 4 8

