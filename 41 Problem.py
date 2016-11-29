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

def isPandigital(num):
    s_num = str(num)
    for i in range(1,len(s_num)+1):
        if not (str(i) in s_num):
            return False
    return True


i = 5
while True:
    if isPandigital(i):
        if isPrime(i):
            print i

    i += 1