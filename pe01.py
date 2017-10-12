'''
Exercise 1

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
2. Print out that many copies of the previous message on separate lines. (Hint: the string '\n' is the same as pressing the ENTER button)
'''

name=input('please enter your name: ')
age=input('please enter your age: ')
year=2017-int(age)+100  #
print(name,'will turn 100 years old in the year',2017-int(age)+100)
#print(name+' will ... year '+str(year)) is the same
#joining up with ',' adds a space in middle
#joining up with '+' adds nothing

#extras
times=int(input('how many copies do you want: '))
print((name+' will turn 100 years old in the year '+str(2017-int(age)+100)) * times)
print((name+' will turn 100 years old in the year '+str(2017-int(age)+100)+'\n')*times)
#message=name+' will turn 100 years old in the year '+str(2017-int(age)+100)+'\n'
#print(message*times)

#ONLY for string 'print(...*times)' means to print some copies of the string