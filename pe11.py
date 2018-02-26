'''
Exercise 11 (and Solution)

Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
'''

from math import sqrt
a=int(input('Enter a number to check whether it is a prime number: '))
b=int(sqrt(int(a)))+1
print(b)
prime=1
for c in range(2,b):
    if a%c==0:
        print(c,int(a/c))
        prime=0
if prime==1:
    print(a,'is a prime number.')
else:
    print(a,'is not a prime number')