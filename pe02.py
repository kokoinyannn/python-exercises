'''
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

num=int(input('Enter a number: '))
result=num%2
if result==0:
    print('EVEN')
else:
    print('ODD')
#pay attention to the two ':' !!!
#pay attention to the indent !!!

#extras
result_2=num%4
if result_2==0:
    print(str(num)+' can be divided evenly by 4.')
else:
    print(str(num)+' cannot be divided evenly by 4.')

check=int(input('Enter another number to check: '))
result_3=num%check
if result_3==0:
    print(str(num)+' can be divided evenly by '+str(check)+'.')
else:
    print(str(num)+' cannot be divided evenly by '+str(check)+'.')