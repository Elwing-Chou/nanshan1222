# tkinter(Simple GUI)
# PyQT(Complicate GUI)
# 物件導向(自訂型態)
# 自訂型態: 值/函式
class Person:

    def __init__(self, w, h):
        self.height = h
        self.weight = w

    def cbmi(self):
        return self.weight / (self.height / 100) ** 2

p1 = Person(75, 174)
print(p1.cbmi())
p2 = Person(80, 180)
print(p2.cbmi())
