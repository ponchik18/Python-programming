# Класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первый метод: создайте переменную и выведите её.
# Второй метод: верните сумму 2-ух глобальных переменных.
# Третий метод: верните результат возведения первой динамической
# переменной во вторую динамическую переменную.
# Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a.
import math


class Example:
    first_global = "Hello"
    second_global = "World"

    def __init__(self, new_first, new_second):
        self.first_dynamic = new_first
        self.second_dynamic = new_second

    def create_variable(self, variable):
        self.variable = variable
        print(self.variable)

    def sum_global_variable(self):
        return self.first_global + self.second_global

    def erection_degree(self):
        return math.pow(self.first_dynamic, self.second_dynamic)


exp = Example(5, 5)
print(exp.sum_global_variable())
exp.create_variable([True, False, 34, "Minsk"])
print(exp.erection_degree())

