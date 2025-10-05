
total_hours=0
current = 1

while True:
     number_of_days = int(input("Введите количество дней: "))
     if 1<=number_of_days<=7:
         break
     print("Данные некорректны!")


while current <= number_of_days:
    hours = int(input("Введите количество часов:"))
    total_hours += hours
    current+=1


print(f"Общее количество часов - {total_hours}")

