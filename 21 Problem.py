def d(x):
    sum = 0
    i = 1
    for i in range(1,x):
        if x % i == 0:
            sum += i
    return sum

n = 1
sum = 0
while n < 10000:
    a = d(n)
    if (n != a) and d(a) == n:
        sum += n
    n += 1

print sum