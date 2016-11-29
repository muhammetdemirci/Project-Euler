def digit_num(num):
    digitnum = 0
    while num > 0 :
        num = num / 10
        digitnum += 1

    return digitnum


index = 0
while True:        
