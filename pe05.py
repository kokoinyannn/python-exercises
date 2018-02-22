'''
Exercise 5

Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
nl=[]
for c in a:
    if c in b and not c in nl:
        nl.append(c)
print('nl =', nl)

#extra1
import random
len1=random.randint(10,20)
len2=random.randint(10,20)
rand_a=[]
rand_b=[]
nl2=[]
while len(rand_a)<len1:
    rand_a.append(random.randint(0,50))
else:
    print('rand_a =', rand_a)
while len(rand_b)<len2:
    rand_b.append(random.randint(0,50))
else:
    print('rand_b =', rand_b)
for c in rand_a:
    if c in rand_b and not c in nl2:
        nl2.append(c)
print('nl2 =', nl2)