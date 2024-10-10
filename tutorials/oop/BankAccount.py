class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, money):
        self.balance = self.balance + money
        return self.balance

    def withdraw(self, money):
        self.balance = self.balance - money
        return self.balance
