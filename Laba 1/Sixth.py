import random

count = int(0)
while True:
    count = int(input("Введите количество чисел(до 40) в списке (P.S. числа сгенерируются автоматически): "))
    if count < 0 or count > 40:
        print("Неправильный ввод! Повторите заново...")
    else:
        break
numbers = list()
for index in range(count):
    numbers.append(random.randint(-5, 10))

const_numbers = tuple(numbers)
print(const_numbers)

index = int(0)
for it in const_numbers:
    if it < 0:
        print("Индекс первого отрицательного элемента равен '%d', а сам элемент '%d'" % (index, it))
        break
    index += 1
if index == len(const_numbers):
    print("В кортеже отсутвуют отрицательные элементы...")