'''
Exercise 14

Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

def minus_dup(list_a):
    result=[]
    for c in list_a:
        if c not in result:
            result.append(c)
    return result
    
def set_dup(list_a):
    result=set(list_a)
    return result

from random import randint
len_a=randint(1,20)
a=[]
while len(a)<len_a:
    r=randint(0,99)
    a[len(a):len(a)+1]=[r,r]
b=minus_dup(a)
c=set_dup(a)
print(a)
print(b)
print(c)