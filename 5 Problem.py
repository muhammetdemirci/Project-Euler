def IsDivisiblefrom1to20(sayi):
    for i in range(19):
        if sayi%(i+1) != 0:
            return "false"
    return "true"



buldu = "false"
x = 0
while buldu == "false":
    x += 1
    if IsDivisiblefrom1to20(x) == "true":
        buldu = "true"

print x
