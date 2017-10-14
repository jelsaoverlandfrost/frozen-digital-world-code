class Account(object):
    def __init__(self, name, account_number, amount):
        self.name = name
        self.account_number = account_number
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        self.amount -= amount

    def __str__(self):
        return '%s, %s, balance: %d' % (self.name, self.account_number, self.amount)


a1 = Account('John Olsson', '19371554951', 20000)
a2 = Account('Liz Olsson', '19371564761', 20000)
a1.deposit(1000)
a1.withdraw(4000)
a2.withdraw(10500)
a1.withdraw(3500)
print a1
print a2
