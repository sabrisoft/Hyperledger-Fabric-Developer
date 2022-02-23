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
        
class DevAccount(Account):
  def __init__(self, id,name, balance):
  	Account.__init__(self, id,name, balance)
     
  def getBalance(self):
        return f"{self.name}'s account. Balance: {self.balance}"

  def dotransfer(self, amount, name):
        self.balance = self.balance - amount
        name.balance = name.balance + amount 
        return name.balance
        

#----FIRST ACCOUNT SET THE ACCOUNT BALANCE (abc)---
abc = DevAccount("7898887777","abc",0)
abc.deposit(1000)

#----SECOND ACCOUNT SET THE ACCOUNT BALANCE (mat)---
mat = DevAccount("7898887778","mat",159)

#----TRANSFER MONEY FROM MAT TO ABC---
mat.dotransfer(11, abc)

#"----CHECK ACCOUNT HOLDER BALANCE!!---
print(abc.getBalance())
print("---------------")
print(mat.getBalance())
