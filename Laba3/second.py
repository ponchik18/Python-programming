# Создать текстовый файл (не программно). Построчно записать
# названия цветов и их стоимость (не менее 10 строк). Вывести на экран все
# цветы, стоимость которых меньше 5 рублей, от 5 до 10 рублей и выше 10
# рублей. Вывести на экран названия цветов, с минимальной стоимостью.
# Пример файла:
# Роза 12
# Гвоздика 5– 3 балла
def read_all_line(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


def create_dictionary(list_of_item):
    flowers_dict = dict()
    for line in list_of_item:
        string = line.replace("\n", '')
        info_list = string.split(" ")
        flowers_dict.update({info_list[0]:int(info_list[1])})
    return flowers_dict


file = "flowers_store.txt"
try:
    list_of_flowers = read_all_line(file)
    dictionary = create_dictionary(list_of_flowers)
    print("Цветы, стоимостью до 5 рублей:")
    for key in dictionary:
        if dictionary[key] < 5:
            print("\t%s %d" % (key, dictionary[key]))
    print("Цветы, стоимостью от 5 до 10 рублей:")
    for key in dictionary:
        if 5 <= dictionary[key] < 10:
            print("\t%s %d" % (key, dictionary[key]))
    print("Цветы, стоимостью до 5 рублей:")
    for key in dictionary:
        if dictionary[key] >= 10:
            print("\t%s %d" % (key, dictionary[key]))
except IOError:
    print('Файл "%s" не найден!' % file)
