primenumber = [2]
def isPrime(num):

    for prime in primenumber:
        if num % prime == 0:
            return False

    i = primenumber[len(primenumber)-1]
    while i < num / 2:
        if num % i == 0:
            return False
    primenumber.append(num)
    return True

def istruncatable(num):
    copynum = list(str(num))
    for i in range(len(copynum)-1):
        del copynum[0]
        if not isPrime(int("".join(copynum))):
            return False

    return True


print istruncatable(37)