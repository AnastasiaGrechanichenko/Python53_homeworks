import random


num = random.randint(0, 2)
action = int(input("Введите число от 0 до 2(0-камень, 1-ножницы, 2-бумага) "))


while True:
    if num == 0 and action == 1 or num == 1 and action == 0:
        print("Победил камень!")
        if num < action:
            print("Компьютер выиграл!")
        else:
            print("Выиграл игрок!")
    elif num == 1 and action == 2 or num == 2 and action == 1:
        print("Победили ножницы!")
        if num < action:
            print("Компьютер выиграл!")
        else:
            print("Выиграл игрок!")
    elif num == 2 and action == 0 or num == 0 and action == 2:
        print("Победила бумага!")
        if num < action:
            print("Выиграл игрок!")
        else:
            print("Компьютер выиграл!")
    elif num == action:
        print("Ничья")
    continuation = input("Желаете продолжить игру(да/нет)?").lower()
    if continuation == 'да':
        num = random.randint(0, 2)
        action = int(input("Введите число от 0 до 2(0-камень, 1-ножницы, 2-бумага)"))
    elif continuation == 'нет':
        break

