
sumofsquares = 0
squaresofsum = 0
totalsum = 0

for i in range(101):
    sumofsquares = sumofsquares + (i * i)
    totalsum = totalsum + i

squaresofsum = totalsum * totalsum

difference =  sumofsquares - squaresofsum

print difference
