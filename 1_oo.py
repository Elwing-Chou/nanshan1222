# tkinter(Simple GUI)
# PyQT(Complicate GUI)
# 物件導向(自訂型態)
# 自訂型態: 值/函式
class Person:
    def cbmi(self):
        return self.weight / (self.height / 100) ** 2


p1 = Person()
p1.height = 175
p1.weight = 75
print(p1.cbmi())
