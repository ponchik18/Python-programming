
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        x = (-1 * b) / (2 * a)
        return x
    if d < 0:
        raise Exception("Дискриминат меньше нуля, вычисление корня невозможно")

    else:
        x1 = ((-1 * b) - d ** 0.5) / (2 * a)
        x2 = ((-1 * b) + d ** 0.5) / (2 * a)
        return min(x1, x2), max(x1, x2)


try:
    a = int(input("Введите коэффициент а: "))
    b = int(input("Введите коэффициент b: "))
    c = int(input("Введите коэффициент c: "))
    print(solve(a, b, c))
except ValueError:
    print("Введён неверный тип")
except Exception as exp:
    print(exp)
finally:
    print("Конец программы")

