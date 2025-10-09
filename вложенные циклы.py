#1
number = int(input("Введите размер: "))
for i in range(number):
    spaces = '  ' * i
    stars = '* ' * (2 * (number - i) - 1)
    print(spaces + stars)


for i in range(number - 2, -1, -1):
    spaces = '  ' * i
    stars = '* ' * (2 * (number - i) - 1)
    print(spaces + stars)


#3
n = int(input("Введите размер: "))
for i in range(1, n, 2):
    i = ' ' * ((n - i)//2)  + '*' * i
    print(i)
for i in range(n, 0, -2):
    i = ' ' * ((n - i)//2)  + '*' * i
    print(i)


