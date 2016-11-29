def find_num_of_primefactors(num):
    numofprime = 0
    i = 2
    while num > 1:
        if num % i == 0:
            num = num / i
            if num % i != 0:
                numofprime += 1
        else:
            i += 1

    return numofprime


def isfirst_four_consequtive(num):
    if find_num_of_primefactors(num) == 4 :
        if find_num_of_primefactors(num+1) == 4 and find_num_of_primefactors(num+2) == 4 and find_num_of_primefactors(num+3) == 4:
            return True
    else:
        return False



i = 10
while True:
    if isfirst_four_consequtive(i):
        print i
        break
    else:
        i += 1

