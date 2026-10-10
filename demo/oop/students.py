from abc import ABC, abstractmethod


# Abstract class
class Student(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print('Name    : ', self.name)
        print('Email   : ', self.email)

    def set_email(self, email):
        self.email = email

    # Abstract method
    @abstractmethod
    def getmarks(self):
        pass


class PythonStudent(Student):
    def __init__(self, name, email, labmarks):
        super().__init__(name, email)
        self.labmarks = labmarks

    def getmarks(self):
        return self.labmarks

    def show(self):
        super().show()
        print('Lab Marks : ', self.labmarks)


class JavaStudent(Student):
    def __init__(self, name, email, theorymarks):
        super().__init__(name, email)
        self.theorymarks = theorymarks

    def getmarks(self):
        return self.theorymarks

    def show(self):
        super().show()
        print('Theory Marks : ', self.theorymarks)


# s = Student('Joe','joe@gmail.com')
ps = PythonStudent('Marshall', 'marshall@gmail.com', 80)
js = JavaStudent('Scott', 'scott@gmail.com', 75)

ps.show()
js.show()
print(ps.getmarks())
print(js.getmarks())
