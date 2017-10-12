'''
Exercise 3

Take a list, say for example this one:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#i=0
print('a has',len(a),'elements')
#for i in range(len(a)) :
#    if int(a[i]) < 5:
for i in a:
    if i<5:
        print(i)
#        i=i+1
#    else:
#        i=i+1
#'for i in a' can directly represent the elements in a
#usage of 'for' is different from C language: for ... in ...
 
#extras
a = [1, 101, 2, 31, 5, -8, 13, 21, 6, 55, 89]
b=[]
print('a has',len(a),'elements')
for i in a:
    if i<10:
        b.append(i)
print('b has',len(b),'elements','\n',b)
#to define an empty array: b=[]
#array.append(sth u want to add)

num=int(input('Enter a number: '))
c=[]
for i in a:
    if i<num:
        c.append(i)
d=sorted(c)
print(d)
#c.xxx只用于对array 'c' 进行操作，比如c.sort()对c进行排序，但不能作为函数引用，如果写成d=c.sort(); print(d)会出错