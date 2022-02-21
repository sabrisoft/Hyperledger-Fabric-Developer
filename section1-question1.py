def kira(n):
    val = 1
    for no in range(2, n + 1):
        val *= no
    return val

number = 100
print("Hasil :",number,":",kira(number))
  
print("----------------------")
  
jumlah_digit = 0
for digit in str(kira(number)):
  jumlah_digit += int(digit)

print("Jumlah Digit :",jumlah_digit)


print("----------------------")
