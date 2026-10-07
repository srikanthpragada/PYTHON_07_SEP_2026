class Course:
    # Class attributes or static attributes
    taxrate = 12

    def __init__(self, title, fee):
        # Object attributes
        self.title = title
        self.fee = fee

    def show(self):
        print('Title : ', self.title)
        print('Fee   : ', self.fee)

    def getnetfee(self):
        tax = self.fee * Course.taxrate // 100
        return self.fee + tax

    def changefee(self, fee):
        self.fee = fee

    @staticmethod
    def gettaxrate():
        return Course.taxrate


print(Course.gettaxrate())
c1 = Course("Gen AI", 10000)
# c1.fee = 12000
c1.changefee(15000)
c1.show()
c2 = Course("AWS", 5000)
print(c2.getnetfee())
