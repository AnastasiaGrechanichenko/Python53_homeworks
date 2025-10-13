# Создать два списка с произвольными значениями
# Первый список размером 5 элементов, второй 8 элементов
# 1. Найти все уникальные элементы первого списка и вывести их на экран


list1 = [1,6,76,6,51]
list2 = [100,90,45,51,72,7,76,4]

for i in range(len(list1)):
    counter = 0
    for j in range(len(list1)):
        if list1[i]==list1[j]:
            counter+=1
    if counter == 1:
        print(list1[i],end = ' ')


#2 Вывести все общие значения для двух списков без повтора


for i in range(len(list1)):
    flag_same = False
    for j in range(len(list2)):
        if list1[i]==list2[j]:
           flag_same  = True
           break

    if flag_same:
        was_flag = False
        for j in range(i):
            if list1[j] == list1[i]:
                was_flag = True
                break
        if not was_flag:
            print(list1[i], end=" ")

# 3. Все повторяющиеся значения первого списка заменить на 0
duplicates_index = []

for i in range(len(list1)):
    counter = 0
    for j in range(len(list1)):
        if list1[i] == list1[j]:
            counter+=1
    if counter > 1:
        duplicates_index.append(i)
for k in duplicates_index:
    list1[k] = 0

print(list1)
# 4. Определить в каком списке среднее значение элементов больше
summ1=0
summ2=0
for i in list1:
    summ1+=i
for j in list2:
    summ2+=j
if summ1/len(list1) > summ2/len(list2):
    print("В 1 списке среднее арифметическое больше")
else:
    print("В 2 списке среднее арифметическое больше")
# 5. Создать два списка одинакого размера но с разными значениями
# Поменять значения этих списков друг с другом в соответствии с их позициями
list3=[1,2,3,4,5]
list4=[10,20,30,40,50]

for i in range(len(list3)):
    list3[i], list4[i] = list4[i], list3[i]
print(list3,list4)






















