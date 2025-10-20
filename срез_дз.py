import random
#Контрольный срез по Python
#1 Пользователь вводит 4 числа, найти наименьшее из них.


number1=int(input("Введите число:"))
number2=int(input("Введите число:"))
number3=int(input("Введите число:"))
number4=int(input("Введите число:"))
minimum=number1
if number1 > number2:
    minimum = number2
if number2 > number3:
    minimum = number3
if number3 > number4:
    minimum = number4


print(minimum)

# (2б) Вывести все целые числа кратные 3 в диапазоне от 0 до - 25
# (условие в цикле использовать нельзя)!

for i in range(0,26,-3):
    print (i,end = " ")


# (2б) Пользователь вводит сторону квадрата. Вывести треугольник вписанный в квадрат сл. образом:
# * * * *
#   * * *
#     * *
#       *

side = int(input("Введите сторону квадрата: "))
for i in range(side):
    print(("  "*i) + ("* "*(side-i)))

# (3б) Пользователь вводит числа до тех пор, пока не введет 0.
# Подсчитать среднее арифметическое введенных чисел.

summa=0
counter=0
while True:
    n = int(input())
    if n==0:
        print(summa/counter)
        break
    summa+=n
    counter+=1

# (3б) Создать список из 10 элементов, заполнить его случайными
# числами в заданном пользователем диапазоне

list1=[0]*10
_min=int(input("Введите начало диапазона: "))
_max=int(input("Введите конец диапазона: "))
if _min>_max:
    _min,_max=_max,_min
for i in range(len(list1)):
    list1[i]=random.randint(_min,_max)
print(list1)

list2 = [random.randint(_min,_max) for i in range (10)]
print(list2)
# (3б) Определить индекс минимального элемента списка

_minimum=list2[0]
min_index=0
for i in range(1, len(list2)):
    if list2[i]< _minimum:
        minimum=list2[i]
        min_index=i
print(min_index)



# (3б) Напишите функцию, принимающую два одинаковых по размеру списка.
# Первый список проинициализирован, второй пустой.
# Функция должна полностью скопировать элементы первого списка во второй.

def list_copy(list1, list2):
    for i in range (len(list1)):
        list2[i]=list1[i]

print(list_copy(list1,list2))

# (4б) Напишите функцию, добавляющую элемент в i-ю позицию списка (возвращает новый список).
def insert(_list,_element,_index):
    list1 = []
    for i in range(_index):
        list1.append(_list[i])
    list1.append(_element)
    for i in range(_index, len(_list)):
        list1.append(_list[i])
    return list1


list4=[1,2,3]
print(list4)


# (6б) Используя готовые методы списков:
# Написать функцию, которая будет создавать список размером n
# и заполнять его числами в диапазоне от a до b.
# Написать функцию, принимает список и число и удаляет из списка все вхождения этого числа.

def create_list(size, a,b):
    return [random.randint(a, b) for i in range(size)]

list5 = create_list(10,10,999)
print(list5)
#
list6 = [2,4,3,5,23,4,2,2,4,3]
n=2
#
while n in list6:
    list6.remove(n)
print(list6)
def remove_elements(_list, index, n):
    for i in range (n):
        _list.pop(index)

list7=[random.randint(10,99) for i in range (10)]
list6 = [2,4,3,5,23,4,2,2,4,3]
print(list6)
remove_elements(list6, 2,3)
print(list6)
