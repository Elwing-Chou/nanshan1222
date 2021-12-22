class Person:
    def __init__(self, h, w):
        self.height = h
        self.weight = w

    def bmi(self):
        return self.weight / self.height

class SuperPerson(Person):
    def __init__(self, h, w, c):
        Person.__init__(self, h, w)
        self.city = c

    def sbmi(self):
        return 2 * self.weight / self.height

p = SuperPerson(175, 75, "Taipei")
print(p.bmi())
print(p.sbmi())
print(p.city)