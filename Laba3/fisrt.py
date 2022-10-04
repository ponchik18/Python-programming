# Создать программный файл F1 в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
# Скопировать в файл F2 только те строки из F1, которые начинаются с буквы «А». Подсчитать количество слов
# в F2. – 3 балла

F1_file = "F1.txt"
F2_file = "F2.txt"


def get_strings_from_user():
    strings = list()
    while True:
        user_input = input()
        if user_input != "":
            strings.append(user_input+"\n")
        else:
            break
    return strings


def write_into_F1(strings, file_name):
    f1 = open(file_name, "w")
    if not isinstance(strings, list):
        raise ValueError("%s ожидает %s!" % (write_into_F1.__name__, list.__name__))
    if not isinstance(file_name, str):
        raise ValueError("%s ожидает %s!" % (write_into_F1.__name__, str.__name__))
    f1.writelines(strings)
    f1.close()
    return


def write_into_F2():
    f1 = open(F1_file, "r")
    f2 = open(F2_file, "w")
    for line in f1:
        if line[0] == "A" or line[0] == "A":

            print("%s\n" % line.replace("\n", ""), file=f2, end="")
    f1.close()
    f2.close()


user_Strings = get_strings_from_user()
try:
    write_into_F1(user_Strings, F1_file)
    write_into_F2()
    print("Данные успешно записаны в файлы!")
except ValueError as exp:
    print(exp)
except IOError:
    print("Ошибка при работе с файлами '%s' и '%s" % (F1_file, F2_file))
