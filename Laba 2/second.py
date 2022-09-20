import re
import random


def do_action(variable):
    if isinstance(variable, list):
        sum_element = int(0)
        for i in variable:
            if i < 0:
                sum_element += i
        tmp = set(variable)
        variable = list(tmp)
        return sum_element, variable
    elif isinstance(variable, set):
        return len(variable)
    elif isinstance(variable, str):
        return work_with_str(variable)
    elif isinstance(variable, int):
        flag = False
        for i in range(2, variable):
            if variable % i == 0:
                flag = True
        return flag
    else:
        return 0


def work_with_str(variable):
    variable = re.sub(r'\d+', r'', variable)
    result_list = re.split(r'\W+', variable)
    for i in range(len(result_list)):
        if result_list[i] == '':
            result_list.remove('')
    glas_list = ['а', 'о', 'у', 'и', 'ы', 'ё', 'я', 'ю', 'э', 'е']
    count_of_glas = int(0)
    count_of_coglas = int(0)

    for index in range(len(result_list)):
        word = result_list[index]
        for index_of_letter in range(len(word)):
            if word[index_of_letter].lower() in glas_list:
                count_of_glas += 1
            else:
                count_of_coglas += 1

    return count_of_glas, count_of_coglas, max(result_list, key = len)


stringName = 'Адаптивная функция'
while True:
    print("+--------------------------------------------------+")
    print("|{:^50}|".format(stringName))
    print("+--------------------------------------------------+")
    stringMenu =['1)Список чисел',
            '2)Множестов символов',
            '3)Число',
            '4)Строка',
                 '5)Завершить работу']
    for i in range(len(stringMenu)):
        print("|{:^50}|".format(stringMenu[i]))
    print("+--------------------------------------------------+")

    answer = int(0)
    while True:
        try:
            answer = int(input("Ваш выбор--> "))
            if answer < 1 or answer>6:
                raise ValueError("Неверный выбор, попробуйте ещё раз")
            break
        except ValueError as exp:
            print(exp)

    if answer == 1:
        list_of_num = list()
        for i in range(15):
            list_of_num.append(random.randint(-5, 5))
        print(list_of_num)
        sum_num, new_list_of_num = do_action(list_of_num)
        print("Сумма отрицательных элементов равна %d. В списке тееперь нет повторяющих элементо..." % sum_num)
        print(new_list_of_num)

    elif answer == 2:
        string = input("Введите строку: ")
        print("Количество символов равно %d" % (do_action(set(string))))
    elif answer == 3:
        num = int(input("Введите число: "))
        if do_action(num):
            print("Данное число не простое")
        else:
            print("Данное число  простое")
    elif answer == 4:
        string = input("Введите строку: ")
        glas, coglas, max_len_word=do_action(string)
        print("%d гласных и %d согласных букв, максимальное слово: %s"% (glas, coglas, max_len_word))
    elif answer == 5:
        break
    else:
        print("Ошибка, попробуйте заново")
