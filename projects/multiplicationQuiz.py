#python3
#multiplicationQuiz.py -> timed multiplication quiz

import random, time 
import pyinputplus as py

# set questions number variable and correct Answers variable to detect correct answers
questionsNumber = 10
correctAnswers = 0

for questionNumber in range(questionsNumber):
    
    # generate the two numbers in a random way
    numOne = random.randint(0,9)
    numTwo = random.randint(0,9)
    
    # generate the question
    prompt = '%s : %s x %s ='%(questionNumber,numOne,numTwo)
    
    # catching the expected errors 
    try:
        py.inputStr(prompt, allowRegexes=['^%s$'%(numOne*numTwo)], blockRegexes=['.*','Incorrect!'], limit=3, timeout=8)
    except  py.TimeoutException:
        print('you have passed the time.')
    except py.RetryLimitException:
        print('you have passed the limit of tries')
    else:
        print('Correct Answer!')
        correctAnswers += 1
    time.sleep(1)#add one second sleep  for the loop
print('score: %s / %s '%(correctAnswers,questionsNumber))
