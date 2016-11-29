def perms(s):
    pers = []
    if(len(s)==1):
        pers.append(s)
        return pers
    res = ''
    for x in xrange(len(s)):
        res += s[x] + perms(s[0:x] + s[x+1:len(s)])
        pers.append(res)
    return pers

print perms([1,2,34,])