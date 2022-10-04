#Написать функцию для вычисления факториала числа.
def factorial(n):

    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)


number = int(0)
flag = bool(True)
while flag:
    try:
        number = int(input("Введите число для факториала: "))
        if number < 0:
            raise ValueError("Неправильно введено число, попробуйте ещё раз")
        else:
            flag = bool(False)
    except ValueError as exp:
        print(exp)
print("Факториал %d = %d " % (number, factorial(number)))