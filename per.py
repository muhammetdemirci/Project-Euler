def per(liste):
    liste = [[a, b ,c]
             for a in liste
             for b in liste
             for c in liste
             if (a != b and b != c and a != c)
             ]
    return liste

def primeproducts(num):
    products = [ ]
    i = 2
    while num > 1:
        if num % i == 0:
            num = num / i
            products.append(i)
        else:
            i += 1
    return products

def ispandigital(num):
    strnum = str(num)
    for c in range(0,len(strnum)):
        if strnum[c] in strnum[c+1:]:
            return False
    return True

def findtwoproducts(num):
    products = primeproducts(num)


print per([2,3,4])

print primeproducts(12)

print ispandigital(1233)


i = 121
while True:
    if ispandigital(i):
        print ispandigita
    else:
        i += 1