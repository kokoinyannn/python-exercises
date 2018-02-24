'''
Exercise 8

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''

running=1
while running==1:
    a=input('player 1: ')
    b=input('player 2: ')
    valid_input=['rock', 'paper', 'scissors']
    while not (a in valid_input and b in valid_input):
        a=input('player 1 (please choose from rock, paper, scissors): ')
        b=input('player 2 (please choose from rock, paper, scissors): ')
    if a==b:
        print('Draw!')
    elif (a=='rock' and b=='scissors') or (a=='scissors' and b=='paper') or (a=='paper' and b=='rock'):
        print('player 1 won')
    else:
        print('player 2 won')
    restart=input('Start over? (y/n) ')
    while restart!='y' and restart!='n':
        restart=input('Valid input! Start over? (y/n) ')
    if restart=='y':
        running=1
    else:
        running=0