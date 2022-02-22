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
