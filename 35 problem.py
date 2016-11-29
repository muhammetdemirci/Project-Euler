primenumber = [2,3,4]
def isPrime(num):

    for prime in primenumber:
        if num % prime == 0:
            return False

    for i in range(primenumber[len(primenumber)-1],num/2):
        if num % i == 0:
            return False
    primenumber.append(num)
    return True

def get_allrotation(num):
    snum = str(num)
    liste = [int(a+b+c)
             for a in snum
             for b in snum
             for c in snum
             if (a != b and b != c and a != c)
             ]

    return liste


def isPrime_for_all_rotation(n):
    strprime = str(n)
    for i in range(0,len(strprime)+1):
        strprime = strprime[1:] + strprime[0]
        if not isPrime(int(strprime)):
            return False
    return True

n = 2
x = 0
sum = 0
while n < 1000000:
    if isPrime(n):
        if isPrime_for_all_rotation(n):
            print n
            x += 1


    n += 1

print  x