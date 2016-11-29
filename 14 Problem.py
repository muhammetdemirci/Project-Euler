
x = 2
longestsequence = 0
lonstart = 2
while x < 1000000:
    n = x
    seq = 0
    while n != 1:
        if n % 2 == 0:
            seq += 1
            n = n / 2
        else:
            seq += 1
            n = 3 * n + 1
    if seq > longestsequence:
        longestsequence = seq
        lonstart = x
    x += 1
print lonstart