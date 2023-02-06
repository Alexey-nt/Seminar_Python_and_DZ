# Задача №17. Дан список чисел. 
# Определите, сколько в нем встречается различных чисел. 
# Input: [1, 1, 2, 0, -1, 3, 4, 4] 
# Output: 6
'''
my_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(f'Ваш список чисел => {my_list}')
print(f'В вашем списке встречается {len(set(my_list))} различных элементов')
'''

# Задача №19. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  
# K – положительное число. 
# Input:   [1, 2, 3, 4, 5] k = 3 
# Output:  [4, 5, 1, 2, 3]

# Решение № 1
'''
my_list = [1, 2, 3, 4, 5]
k = int(input('Введите кол-во элементов, на которое нужно сдвинуть числа: '))
print(f'Начальная последовательность: {my_list}')
while k > 0:
    my_list.append(my_list[0])
    my_list.remove(my_list[0])
    k -= 1
print(f'Смещенная последовательность: {my_list}')
'''
# Решение № 2
'''
from random import randint

n = int(input('Введите длину списка: '))
my_list = [randint(1, 100) for i in range(n)]
print(my_list)

k = int(input('Введите кол-во элементов, на которое нужно сдвинуть числа: '))
while k > 0:
    my_list.append(my_list[0])
    my_list.remove(my_list[0])
    k -= 1
print(f'Смещенная последовательность: {my_list}')
'''
# Решение № 3
'''
your_list = [int(input('Введите элемент: ')) for i in range(int(input('Введите кол-во элементов списка: ')))]
k = int(input('Введите кол-во элементов, на которое нужно сдвинуть числа: ')) % len(your_list)
print(your_list)
k_list = your_list[k:] + your_list[:k]
print(k_list)
'''
# Задача №21. Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Решение № 1
'''
my_list = [{"V": "S001"}, 
           {"V": "S002"},
           {"VI": "S001"}, 
           {"VI": "S005"}, 
           {"VII": "S005"}, 
           {"V":"S009"}, 
           {"VIII":"S007"}]

my_list1 = set()

for i in my_list:
    for value in i.values():
        my_list1.add(value)

print(my_list1)
'''
# Решение № 2
'''
def unic_values(lst):
    unic_values = set()
    for dict in lst:
        for value in dict.values():
            unic_values.add(value)
    return unic_values

input_list = [{"V": "S001"}, 
            {"V": "S002"},
            {"VI": "S001"},
            {"VI": "S005"},
            {"VII": "S005"},
            {"V":"S009"},
            {"VIII":"S007"}]
print(unic_values(input_list))
'''
# Решение № 3
'''
list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
list_values = {tuple(i.values())[].strip() for i in list_dict}
print(list_values)
'''
# Задача №23. Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3] 
# Output: 2 (-1 < 5, 2 < 3)

# Решение № 1
'''
def count_larger_than_previous(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1
    return count
    
array = [0, -1, 5, 2, 3] 
print(count_larger_than_previous(array))
'''
# Решение № 2
'''
from random import randint

my_list = [randint(-10, 10) for _ in range(randint(1, 10))]
print(my_list)

count = 0
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        count += 1

print(count)
'''
# Решение № 3
'''
from random import randint

my_list = [randint(-10, 10) for _ in range(randint(1, 10))]
print(my_list)

new_list = [f'{my_list[i]} > {my_list[i - 1]}' for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(*new_list, sep=' || ')
print(len(new_list))
'''