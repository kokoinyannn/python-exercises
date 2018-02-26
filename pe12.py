'''
Exercise 12 (and Solution)

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''

def firstnlast():
    from random import randint
    len_a=randint(1,20)
    a=[]
    while len(a)<len_a:
        a.append(randint(0,99))
    c=[a[0], a[len(a)-1]]
    print('a =',a,'\nc =',c)

firstnlast()