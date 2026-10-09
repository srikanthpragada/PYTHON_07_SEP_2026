# Superclass
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

# Subclass
class OnsiteEmployee(Employee):
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance

    # Overriding
    def get_salary(self):
        return self.salary + self.allowance

    def set_allowance(self, allowance):
        self.allowance = allowance

e = Employee("Roberts", 50000)
oe = OnsiteEmployee("David", 55000, 20000)
print(e.get_salary())
print(oe.get_salary())

