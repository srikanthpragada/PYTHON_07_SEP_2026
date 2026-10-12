class InvalidAmountError(Exception):
    def __str__(self):
        return "Invalid Transaction Amount!"


class SavingsAccount:
    minbal = 10000

    def __init__(self, acno: int, customer: str, balance=0):
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount: int):
        if amount <= 0:
            raise InvalidAmountError()

        self.balance += amount

    def withdraw(self, amount: int):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            raise ValueError('Insufficient Balance!')

    @property
    def current_balance(self):
        return self.balance

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal


print(SavingsAccount.getminbal())

s = SavingsAccount(1, "Scott", 50000)

try:
    s.deposit(-10000)
    s.withdraw(120000)
except InvalidAmountError as ex:
    print(ex)
except ValueError as ex:
    print('Error :', ex)
print(s.current_balance)
