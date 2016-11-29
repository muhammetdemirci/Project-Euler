def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def stPrime(sayi):
    primenumbers = []
    i = 2
    while len(primenumbers) < sayi:
        if isPrime(i):
            primenumbers.append(i)
            print i
            i = i + 1
        else:
            i = i + 1

    
            
print stPrime(10001)

    
