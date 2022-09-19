
first_num = int(0)
second_num = int(0)
while True:
    first_num = int(input("Введите начало числового диапазон: "))
    second_num = int(input("Введите конец числового диапазона: "))
    if second_num < 2 or first_num < 1 or second_num < first_num:
        print("Ошибка ввода данных, давайте заново")
        continue
    else:
        break

result = set()
for value in range(first_num, second_num):
    flag = False
    for i in range(2, value):
        if value % i == 0:
            flag = True
    if not flag:
        result.add(value)
if len(result) == 0:
    print("В данном диапазоне нет простых чисел")
else:
    print(result)



