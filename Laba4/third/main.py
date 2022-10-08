from Stationery import Stationery, Pen, Pencil, Handle
try:
    pen = Pen()
    pen.draw()
    pencil = Pencil()
    pencil.draw()
    handle = Handle()
    handle.draw()
    stationary = Stationery()
except TypeError as exp:
    print(exp)
