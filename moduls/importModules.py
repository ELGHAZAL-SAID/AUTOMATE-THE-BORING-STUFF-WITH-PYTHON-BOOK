from random import randint,choice
import sys

#test 

for i in range(5):
    # print(rm.randint(0,100))
    list = randint(10,524585)
    print(list)
    sys.exit()


while True:
    print('Type exit.')
    response =input()
    if response == 'exit':
        sys.exit()
    print('You typed '+response+'.')

randomNum = randint(1, 20)
i = 1
print('I am thinking for a number between 1 and 20.')
print('-------------------------------------------------------you have 6 Times to guess')

while True:
    print('Take a guess :')
    response = input()
    if  randomNum == int(response):
        print('Good job ! You guessed my number in '+ str(i) + 'guesses')
        sys.exit()
    elif int(response) >randomNum:
        print('Your guess is too hight')
    elif int(response) <randomNum:
        print('Your guess is too low')
    print("---------------still have "+str(6-i)+' Times to guess')
    i = i + 1
    if i > 6 :
        print("----------------- Your Luck has been ended. ------------------------" )
        break

This is a guess the number game.

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
# This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


for i in range(1, 7):
    print('now you have '+str(7-i)+' chances')
    print('Guess my number :')
    response = int(input())
    
    if randomNum < response:
        print('it is too high')
    elif randomNum > response:
        print('it is too low')
    else:
        break
    

if randomNum == response:
    print('Good job! you guessed my number in the '+str(i)+' chance')
    sys.exit()
else :
    print("--------------------------------------------your luck pocket has been finished, my number was "+str(randomNum))

print('ROCK, PAPER, ScISSORS')
Wins = 0
Losses = 0
Ties = 0

list = ['r','p','s']
print('welcome to Rock PAPER SCISSOR GAME')

while True:
    print(str(Wins)+"Wins, "+str(Losses)+'Losses, '+str(Ties)+' Ties')
    
    randomMove = choice(list)
    
    print('Enter your move: (r) for rock (p)for paper (s) for scissors or (q) for quit')
    choices = input().lower() #answer 
    
    if choices not in list:
        print('incorrect input, try again.')
        continue 

    #choices Results
    
    if choices == 'p':
        print('PAPER versus...')
    elif choices == 'r':
        print('ROCK versus...')
    elif choices == 's':
        print('SCISSORS versus...')
    elif choices == 'q':
        break
    
    if randomMove == 'p':
        print('The opponent choice is : Paper')
    elif randomMove == 'r':
        print('The opponent choice is :Rock')
    elif randomMove == 's':
        print('The opponent choice is :Scissor')


    if choices == randomMove:
        print("it is a Tie!")
        Ties = Ties+1
    
    #win possibilities
    
    elif choices == 'p' and randomMove == 'r':
        print('you wine this round')
        Wins = Wins +1
    elif choices == 'r' and randomMove == 's':
        print('you wine this round')
        Wins = Wins +1
    elif choices == 's' and randomMove == 'p':
        print('you wine this round')
        Wins = Wins +1
    
    #win possibilities
    
    elif choices == 's' and randomMove == 'r':
        print('you lose this round')
        Losses = Losses +1
    elif choices == 'p' and randomMove == 's':
        print('you lose this round')
        Losses = Losses +1
    elif choices == 'r' and randomMove == 'p':
        print('you lose this round')
        Losses = Losses +1

    if Wins == 3 or Losses == 3 or Ties ==3:

        if Wins == 3:
            print('we have a winner')
        elif Losses == 3 :
            print('we have a loser')
        elif Ties ==3:
            print('one more time ? (Y/N)')
            answer = input().lower()
            if answer == 'y':
                Wins = 0
                Losses = 0
                Ties = 0
                continue
            elif answer == 'n':
                sys.exit()
        sys.exit()
