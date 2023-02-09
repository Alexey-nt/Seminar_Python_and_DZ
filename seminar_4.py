# Задача №25. Напишите программу, которая принимает на вход строку, 
# и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n. 
# Для решения данной задачи используйте функцию .split()
# Input: a a a b c a a d c d d 
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Решение № 1:
'''
s = 'a a a b c a a d c d d'
s = s .split()
print(s)
result_dic = {}
new_s = []
for i in s:
    if i not in result_dic:
        new_s.append(i)
        result_dic[i] = result_dic.get(i, 0) + 1
    else:
        new_s.append(f'{i}_{result_dic[i]}')
        result_dic[i] = result_dic.get(i, 0) + 1

print(*new_s)
'''
# Решение № 2: (правильное)
'''
text = 'a a a b c a a d c d d'
text = text.split()
result = ''
d = {}
for i in range(len(text)):
    if text[i] not in d:
        d[text[i]] = 1
        result += f'{text[i]} '
    else:
        result += f'{text[i]}_{d[text[i]]} '
        d[text[i]] += 1


print(result)
'''

# Задача №27. Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте. 
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells 
# Output: 13

# Решение № 1: не корректное
'''
n = input("Введите свой текст: ").split()
n = set(n)
count = 0
print(n)

for i in n:
    count +=1
print(count)
'''
# Решение № 2: (правильное)
'''
text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

new_text = text.lower().replace(';', ' ').replace(',', ' ').replace('.', ' ')

print(len(set(new_text.split())))
'''

# Задача №29. Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам. 
# Примечание: Программные коды на следующих слайдах
#   Ваня:                          Петя:
#   n = int(input())               n = int(input())
#   max_number = 1000              max_number = -1
#   while n != 0:                  while n < 0:
#       n = int(input())               n = int(input())
#       if max_number > n:             if max_number < n:
#           max_number = n                 n = max_number
#   print(max_number)              print(n)


