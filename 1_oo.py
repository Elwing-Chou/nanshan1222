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

    def __str__(self):
        return "{}/{}".format(self.weight,
                              self.height)

    def __eq__(self, other):
        return self.weight == other.weight

p1 = Person(75, 174)
# str(p1) -> p1.__str__()
print(p1)
print(p1.cbmi())
p2 = Person(75, 180)
print(p2.cbmi())
# p1.__eq__(p2)
print(p1 == p2)