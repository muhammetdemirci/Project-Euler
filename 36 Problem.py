def Check_palindromic(sayi):
    strsayi = str(sayi)
    lensayi = len(strsayi)
    for i in range(len(strsayi)):
        if strsayi[i] != strsayi[-i - 1]:
            return False
    return True


def dectobin(n):
    number = list(bin(n))
    del number[0]
    del number[0]
    num = "".join(number)
    return num


i = 0
sum = 0
while i < 1000000:
    if Check_palindromic(i):
        if Check_palindromic(dectobin(i)):
            sum += i
    i += 1

print sum
