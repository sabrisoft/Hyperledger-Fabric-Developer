class Account:
   def __init__(self, id,name, balance):
        self.id=id
        self.name=name
        self.balance=balance
        

   def deposit(self, amount):
      if amount > 0:
             self.balance += amount

   def withdraw(self, amount):
      if amount > 0 and self.balance > amount:
            self.balance -= amount
      else:
            print("the amount in your is not sufficent")

   def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"


class DevAccount(Account):
  def __init__(self, id,name, balance):
        self.id=id
        self.name=name
        self.balance=balance
     
  def getBalance(self):
        return self.balance

  def dotransfer(self, amount, name):
        self.balance = self.balance - amount
        name.balance = name.balance + amount 
        return name.balance()

--------------------------------

a1 = DevAccount('7898887777','ALI',20000)
print(a1.getBalance())
print("Balance is : " +str(a1.dotransfer(100, ahmad)))
print("Self Balance is : " +str(a1.getBalance()))
