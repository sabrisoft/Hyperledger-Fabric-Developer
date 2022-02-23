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

#Aturcara ini menunjukkan kefahaman untuk membina class di dalam bahasa Python. 
#Cara mudah adalah menyediakan simulasi transaksi perbankan iaitu terdiri daripada fungsi asas bank in wang (deposit) & pengeleuaran wang (withdraw) 
#serta paparan baki akaun terkini. Kod Class Account dimulakan dengan fungsi initial iaitu setting awal pembolehubah pengguna seperti nama, nokp as id, no akaun (jika ada) 
#dan nama (pemegang akaun bank). Manakala function deposit adalah untuk setting baki awal yang ditambah dengan amaun yang didepositkan. Function withdraw merujukan fungsi untuk urus pengeluaran iaitu baki terkini selepas ditolak dengan amount pengeluaran. Akhir sekali adalah fungsi string (str) iaitu fungsi mudah python untuk menghasilkan output di dalam python (mudah read dan write untuk member di dalam class).
#Simulasi untuk memanggil class account adalah dengan mengistiharkan tiga pembolehubah instance yang memanggil class account iaitu a1,a2 dan a3. Contoh a1 = Account('7898887777','ALI' ,20000). Setelah Instance a1,a2 dan a3 di panggil daripada class account, method atau fungsi di dalam class account boleh digunakan (deposit,withdraw, str). contoh di atas a1.withdraw(4000)...etc.Apabila method ini dipanggil,a1.withdraw(4000) contohnya,baki terkini akan dipaparkan.
#Terima kasih.

