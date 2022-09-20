import random


def enter_matrix_info(string):
    attribute = int(0)
    if not isinstance(string, str):
        raise TypeError("Функция '%s' ожидает строку!" % enter_matrix_info.__name__)
    while True:
        try:
            attribute = int(input("%s: " % string))
            if attribute < 0:
                raise ValueError("Неправильно введены данные, попробуйте ещё раз...")
            break
        except ValueError as exp:
            print(exp)
    return attribute


def create_matrix(row, column):
    # генерация матрицы, элементы заполняются нулями
    if not (isinstance(row, int) or isinstance(column, int)):
        raise TypeError("Функция '%s' ожидает 2 числа!" % create_matrix.__name__)
    matrix = [[0 for x in range(column)] for y in range(row)]
    #заполнение матрицы слуйными числами
    for i in range(row):
        for j in range(column):
            matrix[i][j] = random.randint(-7, 4)
    return matrix


def matrix_change(matrix):
    if not (isinstance(matrix, list) or isinstance(matrix[0], list)):
        raise TypeError("Функция '%s' ожидает матрицу!" % matrix_change.__name__)
    flag_for_all_matrix = [False for y in range(len(matrix))]
    for i in range(len(matrix)):
        flag = False
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                flag = True
        flag_for_all_matrix[i] = flag
    if False in flag_for_all_matrix:
        raise ValueError("Не все строки матрицы содержаться положительный элемент...")
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] *= -1
    return matrix


def print_matrix(matrix):
    if not (isinstance(matrix, list) or isinstance(matrix[0], list)):
        raise TypeError("Функция '%s' ожидает матрицу!" % print_matrix.__name__)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print("%2d " % matrix[i][j], end='')
        print("")


try:
    rows_of_matrix = enter_matrix_info("Введите число строк в матрице")
    columns_of_matrix = enter_matrix_info("Введите число столбцов в матрице")
    result_matrix = create_matrix(rows_of_matrix, columns_of_matrix)
    print_matrix(result_matrix)
    result_matrix = matrix_change(result_matrix)
    print("Новая матрица:")
    print_matrix(result_matrix)
except (TypeError, ValueError) as exp:
    print(exp)



