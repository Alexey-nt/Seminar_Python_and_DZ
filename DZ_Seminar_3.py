# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai . 
# Последняя строка содержит число X 

# N = 5 
# [1 2 3 4 5] 
# X = 3 -> 1 
'''
from random import randint

N = int(input('Введите кол-во элементов массива: '))
A = [randint(0, 10) for i in range(N)]
print(A)

count = 0
X  = int(input('Введите число, которое хотите найти: '))
for i in range(0, len(A)):
    if A[i] == X:
        count += 1
    
if A[i] != X:
        print('Вашего числа нет в получившемся массиве.')
print(f'Число {X} встречается {count} раз.')
'''

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai . 
# Последняя строка содержит число X 

# 5 
# 1 2 3 4 5 
# 6-> 5
'''
from random import randint

N = int(input('Введите кол-во элементов массива: '))
A = [randint(0, 10) for i in range(N)]
print(A)

X  = int(input('Введите ваше число: '))
X_min = 0
X_max = 0
for i in range(0, len(A)):
    if A[0] < X:
        X_min = A[i]
        i += 1
    if A[0] > X:
        X_max = A[i]
        i += 1

print(X_min)
print(X_max)
'''

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так: 
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы. 

# Пример 
# Ввод: ноутбук 
# Вывод: 12
'''
import re

word = input("Введите любое слово: ")
word = word.upper()

rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}

def RusOrEng(word):
    return bool(re.search("[а-яА-Я]", word))

if RusOrEng(word):
    print("Сумма баллов:", sum([k for i in word for k, v in rus.items() if i in v]))
else:
    print("Сумма баллов:", sum([k for i in word for k, v in eng.items() if i in v]))
'''