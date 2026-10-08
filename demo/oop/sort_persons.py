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


persons = [Person("Rossum", 50),
           Person("Joe", 20),
           Person("Gosling", 55)]

for p in sorted(persons):
    print(p)
