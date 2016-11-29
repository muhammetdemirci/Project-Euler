import math



for a in range(1000):
    for b in range(1000):
        c = math.sqrt((a*a) +(b*b))
        if a + b + c == 1000:
            print a*b*c
    
