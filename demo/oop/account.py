class SavingsAccount:
    minbal = 10000
    def __init__(self, acno : int, customer : str, balance = 0):
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount : int):
        self.balance += amount

    def withdraw(self, amount : int):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            print('Sorry! Insufficient Balance!')

    def getbalance(self):
        return self.balance

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal


print(SavingsAccount.getminbal())

s = SavingsAccount(1, "Scott", 50000)
s.deposit(10000)
s.withdraw(20000)
print(s.getbalance())

