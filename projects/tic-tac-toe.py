# tic-tac-toe

import random

theBoard = {'top-L':'1','top-M':'2','top-R':'3',
            'mid-L':'4','mid-M':'5','mid-R':'6',
            'low-L':'7','low-M':'8','low-R':'9'
            }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkPlace(place):
    if place == '1':
        return 'top-L'
    if place == '2':
        return 'top-M'
    if place == '3':
        return 'top-R'
    if place == '4':
        return 'mid-L'
    if place == '5':
        return 'mid-M'
    if place == '6':
        return 'mid-R'
    if place == '7':
        return 'low-L'
    if place == '8':
        return 'low-M'
    if place == '9':
        return 'low-R'

def checkWinner(dic):
    dicList = list(dic.values())
    if  dicList[0:3] == ['X','X','X']:
        return 'X'
    if  dicList[0:3] == ['O','O','O']:
        return 'O'
    if  dicList[3:6] == ['X','X','X']:
        return 'X'
    if  dicList[3:6] == ['O','O','O']:
        return 'O'
    if  dicList[6:9] == ['X','X','X']:
        return 'X'
    if  dicList[6:9] == ['O','O','O']:
        return 'X'

    if dicList[0] == "O" and dicList[3] == "O" and dicList[6] == "O":
        return 'O'
    if dicList[1] == "O" and dicList[4] == "O" and dicList[7] == "O":
        return 'O'
    if dicList[2] == "O" and dicList[5] == "O" and dicList[8] == "O":
        return 'O'
        
    if dicList[0] == "X" and dicList[3] == "X" and dicList[6] == "X":
        return 'X'
    if dicList[1] == "X" and dicList[4] == "X" and dicList[7] == "X":
        return 'X'
    if dicList[2] == "X" and dicList[5] == "X" and dicList[8] == "X":
        return 'X'
        
    if dicList[0] == "O" and dicList[4] == "O" and dicList[8] == "O":
        return 'O'
    if dicList[2] == "O" and dicList[4] == "O" and dicList[6] == "O":
        return 'O'
    if dicList[0] == "X" and dicList[4] == "X" and dicList[8] == "X":
        return 'X' 
    if dicList[2] == "X" and dicList[4] == "X" and dicList[6] == "X":
        return 'X'

def showScore(player1, player2, scoreP1, scoreP2):
    print(player1,":",scoreP1)
    print(player2,":",scoreP2)

player1 = 'robot1'
player2 = 'robot2'

scoreLicht = 0
scoreHyuga = 0 

round = 0
luck = random.randint(0,1)
if luck == 0:
    turn = 'X'
elif luck == 1:
    turn ='O'

print(player1,'your symbol will be X and',player2,'will be O')

while True:
    round = round + 1
    for i in range(9):
        if turn == "X":
            # print('it is',player1,'.\'s turn') 
            while True:
                move = str(random.randint(1,9))
                # move = input()
                if move in theBoard.values():
                    theBoard[checkPlace(move)] = turn
                    break
                else :
                    continue
        elif turn == "O":
            # print('it is',player2,'.\'s turn')    
            while True :
                move = str(random.randint(1,9))
                # move = input()
                if move in theBoard.values():
                    theBoard[checkPlace(move)] = turn
                    break
                else :
                    continue
        if turn == "X":
            turn = 'O'
        else:
            turn = "X"
    winner = checkWinner(theBoard)        
    if winner == 'X':
        scoreLicht += 1
    elif winner == 'O':
            scoreHyuga += 1 
    print('round',round)
    printBoard(theBoard)
    if round == 3:
        showScore(player1,player2,scoreLicht,scoreHyuga)
        if scoreLicht > scoreHyuga:
            print('=====================================================')
            print(player1, 'is the winner ')
            print('=====================================================')
            break
        if scoreHyuga > scoreLicht:
            print('=====================================================')
            print(player2, 'is the winner ')
            print('=====================================================')
            break
        else:
            print('----------------------------------------------------------------------')
            print('No winner in this Game')
            print('----------------------------------------------------------------------')
            break

