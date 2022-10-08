# Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
# 2000}]
# Подсказка: использовать менеджер контекста. – 1 балл (задача на
# оценку 10)


import json


def read_all_line(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def create_dictionary(list_of_item):
    firm_dictionary = dict()
    average_profit = int(0)
    for line in list_of_item:
        string = line.replace("\n", '')
        info_list = string.split(" ")
        future_key = info_list[0]
        future_value = int(info_list[2]) - int(info_list[3])
        average_profit += future_value
        firm_dictionary.update({future_key: future_value})
    profit_dictionary = dict({"average_profit": round(float(average_profit)/len(firm_dictionary), 2)})
    return [firm_dictionary, profit_dictionary]


file = "info_about_firm4.txt"
try:
    list_of_flowers = read_all_line(file)
    list_of_dictionary = create_dictionary(list_of_flowers)
    for item_of_dict in list_of_dictionary:
        for key in item_of_dict:
            print("%s : %.2f" % (key, item_of_dict.get(key)))
    with open("firm.json", "w") as write_f:
        json.dump(list_of_dictionary, write_f)
    with open("firm.json", "r") as read_f:
        info = json.load(read_f)
        print(info)
except IOError:
    print('Файл "%s" не найден!' % file)
except ValueError:
    print('Файл сформирован неправильно! До свидания...')