##Each new term in the FiThe prime factors of 13195 are 5, 7, 13 and 29.

##What is the largest prime factor of the number 600851475143 ?

number = 600851475143
for i in range(600851475143):
     if number % i == 0:
         number = number / i
         print i
