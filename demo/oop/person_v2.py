class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age


p1 = Person("Rossum", 50)

print(Person.__module__)
print(Person.__bases__)
print(p1.__dict__)   # __dict__ is built-in object attribute