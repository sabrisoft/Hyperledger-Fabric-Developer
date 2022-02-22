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



class DevAccount(Account):
  def __init__(self, initial_balance=0, rate=0.1):
     BankAccount.__init__(self, initial_balance)
     self._rate = rate
  def interest(self):
     return self.balance * self._rate
