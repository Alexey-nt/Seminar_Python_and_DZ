
#? Задача №47. Решение в группах У вас есть код, который вы не можете менять 
#? (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать): 
#? transformation = <???> 
#? values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список 
#? transormed_values = list(map(transformation, values)) 
#? Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation. 
#? Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, 
#? а нужно получить его как есть. 
#? Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
'''
#values = [1, 23, 42, 'asdfg'] 

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformation = lambda i: i

transformed_values = list(map(transformation, values)) 
if values == transformed_values:
    print('ok')
else:
    print('fail')

# либо вывод можно сделать через тернарный оператор

print('ok' if values == transformed_values else 'fail')
'''
#? Задача №49. Решение в группах Планеты вращаются вокруг звезд по эллиптическим орбитам. 
#? Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
#? Напишите функцию f ind_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
#? по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды 
#? таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. 
#? Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. 
#? Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
#? Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. 
#? При решении задачи используйте списочные выражения. 
#? Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, 
#? а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна

#? Ввод: orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
#?       print(*find_farthest_orbit(orbits))

#? Вывод: 2.5 10
'''
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
one_lst, two_lst = zip(*orbits)
my_list = []
for i in range(len(one_lst)):
    if one_lst[i]== two_lst[i]:
        my_list.append(0)
    else:
        s = one_lst[i]* two_lst[i]
        my_list.append(s)
# вывод 1 способом:
for i in range(len(one_lst)):
    if my_list[i] == max(my_list):
        print(orbits[i])
# вывод 2 способом:
max_elem = max(my_list)
i_max_elem = my_list.index(max_elem)
print(orbits[i_max_elem])
'''
# Решение № 2:
'''
from math import pi

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

orbits = [i for i in orbits if i[0] != i[1]]
max_square = max([pi * i[0] * i[1] for i in orbits])
max_square_a_b = [i for i in orbits if pi * i[0] * i[1] == max_square]

print(*max_square_a_b)
'''
# Решение № 3:
'''
from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
maximum = max(list(map(lambda x: pi * x[0] * x[1] ,(filter(lambda i: i[0] != i[1], orbits)))))
far = filter(lambda y: pi * y[0] * y[1] == maximum, orbits)
print(*list(*far))
'''

#? Задача №51. Решение в группах. Напишите функцию same_by(characteristic, objects), 
#? которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и 
#? возвращают True, если это так. Если значение характеристики для разных объектов отличается - то False. 
#? Для пустого набора объектов, функция должна возвращать True. 
#? Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
'''
def same_by(characteristic, objects):
    for i in objects:
        if characteristic(i):
            return False
    return True

values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
'''
# Решение № 2:
'''
def same_by(characteristic, objects):
    if not objects:
        return True
    first_value = characteristic(objects[0])
    return all(characteristic(obj) == first_value for obj in objects)

values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
'''
# Решение № 3:
'''
def same_by(func, list1):
    new_list1 = list(filter(func, list1))
    return len(new_list1) == len(list1) or len(new_list1) == 0

values = [2, 4, 6, 8]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
'''