# 1. написать функцию генерирующую список заданного размера
# из случайных значений заданного диапазона

import random


def generate_list(size,b1,b2):
    list1 = []
    counter = 0
    if b1 > b2:
        b1,b2 = b2, b1


    for x in range(b1,b2):
        number = random.randint(b1,b2)
        list1.append(number)
        counter +=1
        if counter == size:
            print(list1)
            break


generate_list(5,10,20)
generate_list(3,1,5)
# 2. написать функцию, возвращающую максимальное значение из списка

list2=[1,2,100,89,106,9,2,8,106]


def return_max(_list):
    maximum = _list[0]
    for x in range(len(_list)):
        if _list[x] > maximum:
            maximum = _list[x]
    return maximum


print(return_max(list2))

# 3. написать функцию, определяющую количество повторяющихся значений списка

def define_repetitions(_list):
    counter = 0

    for i in range(len(_list)):
        flag_met = False
        for j in range(i):
            if _list[i] == _list [j]:
                flag_met = True
                break
        if flag_met:
            counter+=1
    print(counter)


define_repetitions(list2)
# 4. написать функцию, принимающую в качестве параметра список и
# возвращающую новый список, включающий только положительные числа из
# первого списка

def return_positive_list(_list):
    positive = []
    for i in _list:
        if i > 0:
            positive.append(i)
    return positive


list3=[1,2,3,-5,-6,-8,-8,6,6]
print(return_positive_list(list3))

# 5. написать функцию, удаляющую из списка все четные значения

def delete_even(_list):
    last_index=len(_list)-1
    while last_index >= 0:
        if _list[last_index] % 2 == 0:
            del _list[last_index]
        last_index-=1
    print(_list)


delete_even(list3)
# 6. написать функцию, принимающую два списка и возвращающую список содержащий все уникальные элементы
# из этих двух списков

list4=[1,2,3,4,13]
list5=[1,2,3,4,5,6,10,2]


def generate_unique(_list1,_list2):
    unique = list(set(_list1)^set(_list2))
    return unique
print(generate_unique(list4,list5))
