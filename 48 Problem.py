
sum = 0
for i in range(1,1001):
    expo = 1
    for a in range(0,i):
        expo *= i
    sum += expo
    sum = sum % 10000000000


print sum