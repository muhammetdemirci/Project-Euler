sum = 0

dizi= [1,2]
old_number = 1
now_number = 2
while now_number < 4000000:
    
    s = now_number
    now_number = old_number + now_number
    if now_number < 4000000:
        dizi.append(now_number)
    old_number = s


for i in range(len(dizi)):
    
    print(dizi[i])
    if dizi[i]%2==0:
        sum += dizi[i]

print "sum = ",sum
