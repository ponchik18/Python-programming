# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер); в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение; создать экземпляры классов и проверить, что
# выведет описанный метод для каждого экземпляра. – 3 балла

from abc import ABC, abstractmethod


class Stationery(ABC):
    def __init__(self):
        self.__title = "None"

    @abstractmethod
    def draw(self):
        print("Запуск отрисовки - ", end='')


class Pen(Stationery):
    def __init__(self):
        super(Pen, self).__init__()
        self.__title = "ручка"

    def draw(self):
        super().draw()
        print("%s пишет!" % self.__title)


class Pencil(Stationery):
    def __init__(self):
        super(Pencil, self).__init__()
        self.__title = "карандаш"

    def draw(self):
        super().draw()
        print("%s рисует!" % self.__title)


class Handle(Stationery):
    def __init__(self):
        super(Handle, self).__init__()
        self.__title = "маркер"

    def draw(self):
        super().draw()
        print("%s подчёркивает!" % self.__title)
