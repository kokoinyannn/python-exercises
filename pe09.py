'''
Exercise 9

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

from random import randint
quit=0
correct=0
c=0
print('You can always end this game by typing "exit".')
while quit==0:
    a=randint(1,9)
    while correct!=1:
        b=input('Please guess a number from 1 to 9: ')
        while not (b=='exit' or int(b) in range(1,10)):
            b=input('Invalid input! Please guess a number from 1 to 9: ')
        if b=='exit':
            break
            quit=1
        else:
            b=int(b)
            c=c+1
        if b>a:
            print('Too high. Please guess again.')
        elif b<a:
            print('Too low. Please guess again.')
        else:
            correct=1
            print('Cong!')
            print(c, 'guesses')
    q=input('Do you want to exit? (y/n) ')
    while q!='y' and q!='n':
        q=input('Invalid Input! Do you want to exit? (y/n) ')
    if q=='y':
        quit=1
    else:
        correct=0
        c=0