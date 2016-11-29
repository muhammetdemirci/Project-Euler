def IsSameDigit(num):
    strnum1 = str(num)
    strnum2 = str(num * 2)
    strnum3 = str(num * 3)
    strnum4 = str(num * 4)
    strnum5 = str(num * 5)
    strnum6 = str(num * 6)

    if strnum1[0] != "1":
        return False
    if (len(strnum1) != len(strnum2)) or (len(strnum1) != len(strnum3)) or (len(strnum1) != len(strnum4)) or (len(strnum1) != len(strnum5)) or (len(strnum1) != len(strnum6)) :
        return False
    for i in strnum2:
        if not (i in strnum1):
            return False
    for i in strnum3:
        if not (i in strnum1):
            return False
    for i in strnum4:
        if not (i in strnum1):

            return False
    for i in strnum5:
        if not (i in strnum1):

            return False
    for i in strnum6:
        if not (i in strnum1):

            return False
    

    return True

    
durum = False
index = 99
while not durum :
    index += 1
    durum = IsSameDigit(index)
    
    

print index
