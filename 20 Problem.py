factorial= 1
toplam= 0
for i in range (1,100):
    factorial *= i

print factorial

while factorial > 0:
    toplam=toplam + (factorial%10)
    factorial = factorial/10

print toplam
    

