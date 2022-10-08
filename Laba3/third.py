# Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#  Физика: 30(л) 10(лаб)
#  Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:
# 30}– 3 балла
import re


def read_all_line(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def create_dictionary(list_of_item):
    flowers_dict = dict()
    for line in list_of_item:
        string = re.sub(r'[()\n]', r'', line)
        subject = re.split(r":\W*", string)[0]
        string_hour = re.split(r":\W*", string)[1]

        hour_subject_count = int(0)
        for item in string_hour.split(" "):
            hour_subject_count += int(re.sub(r"\D+", r"", item))
        flowers_dict.update({subject: hour_subject_count})
    return flowers_dict


file = "subject.txt"
try:
    list_of_flowers = read_all_line(file)
    dictionary = create_dictionary(list_of_flowers)
    for key in dictionary:
        print("\t%s %d" % (key, dictionary[key]))
except IOError:
    print('Файл "%s" не найден!' % file)