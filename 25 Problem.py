def digitnumber(number):
    digitnumber = 0
    while number > 0:
        number = number/10
        digitnumber += 1
    return digitnumber
print digitnumber(23)

x= 1
oldx=1
sayac=0
while 1==1 :
    y=x
    x= x+oldx
    oldx=y
    sayac +=1
    print x
    print sayac
    if digitnumber(x)==1000:
        print sayac
        
