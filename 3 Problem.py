##prime factor
sayi=600851475143
print sayi
primefactors=[]
for i in range(2,sayi+1):
    while sayi%i == 0:
        sayi=sayi/i
        primefactors.append(i)

print primefactors 
    
    
    
