

def get_zero_division_error():
    num = 4/0
    return


def get_index_error():
    array = list()
    array.index(45)
    return


def get_type_error():
    string = "Hello"
    num = 4
    print(string + num + string)
    return


def get_value_error():
    a = int("eqw")
    return


def get_nothing():
    return


exception_menu = ["Попытка деления на ноль",
                  "Индекс не входит в диапазон элементов",
                  "Несоответствие объекта и типа данных",
                  "Некорректное значение аргумента функции",
                  "Ничего не хочу ;=)"]
print("Веберите исключение которое хотити бросить ")
for i in range(len(exception_menu)):
    print("%d) %s" % (i+1, exception_menu[i]))
while True:
    try:
        answer = int(input("\n Ваш выбор ==> "))
        if answer < 0 or answer > 6:
            raise AssertionError ("Вы ввели число не из допустимого диапазона")
        break
    except ValueError as exp:
        print("Введён неверный тип!")
        print("Попробуйте ещё раз...")
    except AssertionError  as exp:
        print(exp)
        print("Попробуйте ещё раз...")

try:
    if answer == 1:
        get_zero_division_error()
    if answer == 2:
        get_index_error()
    if answer == 3:
        get_type_error()
    if answer == 4:
        get_value_error()
    if answer == 5:
        get_nothing()
        print("Ну значит будем отдыхать ;=)")
except ZeroDivisionError as exp:
    print("Было перехвачено исключение типа %s" % ZeroDivisionError.__name__)
except TypeError as exp:
    print("Было перехвачено исключение типа %s" % TypeError.__name__)
except ValueError as exp:
    print("Было перехвачено исключение типа %s" % ValueError.__name__)
except IndexError as exp:
    print("Было перехвачено исключение типа %s" % IndexError.__name__)
finally:
    print("Вызван блок 'finally'")
    print("На это всё...")
