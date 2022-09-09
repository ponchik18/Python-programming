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
    numbers.append(random.randint(0, 10))

print(numbers)

count_of_pair = int(0)

for i in range(count-1):
    for j in range(i+1, count):
        if numbers[i] == numbers[j]:
            count_of_pair += 1

if count_of_pair == 0:
    print("Совпадений не найдено...")
else:
    print("Найдено %d совпадений! ",count_of_pair)