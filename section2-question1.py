class Account:
  def __init__(self, id,name, balance):
        self.id=id
        self.name=name
        self.balance=balance
  def deposit(self, amount):
      if amount > 0:
             self.balance += amount
      else:
      		 print("Invalid amount!!")
  def withdraw(self, amount):
      if amount > 0 and self.balance > amount:
            self.balance -= amount
      else:
            print("the amount in your is not sufficent")

  def __str__(self):
        return f"{self.name}'s account. Balance: {self.balance}"
        
print("--------instance 1-----")   
a1 = Account('7898887777','ALI',20000)
a1.deposit(100)
print(a1)
a1.withdraw(4000)
print(a1)
a1.withdraw(3500)
print(a1)

print("--------instance 2------")
a2 = Account('8088777777','ABU',30000)
a2.deposit(100)
print(a2)
a2.withdraw(4000)
print(a2)
a2.withdraw(3500)
print(a2)

print("--------instance 3------")
a3 = Account('8088777777','AHMAD',40000)
a3.deposit(100)
print(a3)
a3.withdraw(4000)
print(a3)
a3.withdraw(3500)
print(a3)

