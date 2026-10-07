class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"


p1 = Person("Rossum", 50)
p2 = Person("Rossum", 50)

print(p1 == p2)
print(p1 > p2)


p3 = Person("Gosling", 55)

print(p1)  # p1.__str__()
print(p1.__str__())
