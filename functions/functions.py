# let's start functions
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    

print(getAnswer(random.randint(1,9)))


def A():
    B()

def B():
    print('this is b')
    C()
    D()

def C():
    print("this is C")
    D()
    
def D():
    print("this is D")

    
    
A()


def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
    

spam()
eggs = 50

def spam():
    global eggs
    eggs = 40

spam()  #eggs = 40

print(eggs)