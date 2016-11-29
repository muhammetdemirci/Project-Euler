index = 0
i = 0
for i in range(123456789,987654322):
    index += 1
    if index%1000 == 0:
        print index
    if index == 10:
        break

print i
