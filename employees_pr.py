employees=[]


def add_employee():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    office_number =  int(input("Введите номер кабинета: "))
    phone_number = input("Введите номер телефона: ")
    position = input("Введите должность: ")
    employee=[last_name,first_name,patronymic,office_number,phone_number,position]
    employees.append(employee)


def remove_employee(index):
    employees.pop(index - 1)


def show_employees():
    print("№\t| Фамилия\t| Имя\t| Отчество\t| Кабинет\t| Телефон\t| Должность")
    for i in range(len(employees)):
        print(i + 1, end="\t")
        for j in range(len(employees[i])):
            print("|", employees[i][j], end="\t")
        print()
    print()


def sort_by_surname():
    employees.sort(key = lambda x : x[0])
    print(employees)


def search_by_surname(surname):
    for employee in employees:
        if surname in employee[0]:
            print(*employee)


def show_office(_office):
    print("Фамилия\t| Имя\t| Отчество\t| Кабинет\t| Телефон\t| Должность")
    found = False
    for employee in employees:
        if employee[3] ==_office:
            FIO = employee[0]+ " " + employee[1] + " " + employee[2]
            print (f"Каб. № {_office} - {FIO}")
            found = True


def change_data(index):
    if index < 1 or index > len(employees):
        print("Неверный номер сотрудника.")
        return

    employee = employees[index - 1]
    field = input("Введите номер поля для изменения (1-6): ")
    if field == "1":
        employee[0] = input("Новая фамилия: ")
    elif field == "2":
        employee[1] = input("Новое имя: ")
    elif field == "3":
        employee[2] = input("Новое отчество: ")
    elif field == "4":
        employee[3] = int(input("Новый кабинет: "))
    elif field == "5":
        employee[4] = input("Новый телефон: ")
    elif field == "6":
        employee[5] = input("Новая должность: ")
    else:
        print("Неверный выбор.")
        return

        print("Данные изменены")



if __name__ == '__main__':
    add_employee()
    add_employee()
    show_employees()
    show_office(1)
    remove_employee(2)
    add_employee()
    add_employee()
    add_employee()
    remove_employee(1)
    sort_by_surname()
    search_by_surname("Петров")
    show_employees()



