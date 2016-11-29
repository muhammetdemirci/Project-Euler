def Check_palindromic(sayi):
    strsayi=str(sayi)
    lensayi = len(strsayi)
    for i in range(len(strsayi)):
        if strsayi[i] != strsayi[-i-1]:
            return "false"
    return "true"

print Check_palindromic(9009)

maxpalindrome = 0
for ix in range(100,1000):
    for iy in range(100,1000):
        if Check_palindromic(ix*iy) == "true":
            if ix*iy > maxpalindrome:
                maxpalindrome = ix*iy

print maxpalindrome
    
    
    
