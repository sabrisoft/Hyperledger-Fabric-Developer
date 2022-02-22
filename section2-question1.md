class Account:
    def __init__(self, id,name, balance):
        self.id=id
        self.name=name
        self.balance=balance
       
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"


expected output

>>> from classes import Account
>>> a1 = Account('7898887777','ALI' ,20000)
>>> a2 = Account('8088777777',  'ABU', 20000)
>>> a3 = Account('6799909999',  'AHMAD', 20000)
>>> a1.deposit(1000)
>>> a1.withdraw(4000)
>>> a3.deposit(1000)
>>> a2.withdraw(10500)
>>> a1.withdraw(3500)
>>> ALI's account. Balance: 13500
>>> ABU's account. Balance: 9500
>>> AHMAD's account. Balance: 21000
