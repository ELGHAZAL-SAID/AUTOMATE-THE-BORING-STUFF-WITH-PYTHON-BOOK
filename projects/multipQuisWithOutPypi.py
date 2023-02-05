import random 
import time

print('10 question.\nyou have 3 chances and 8 seconds for every question!')

questionsNumber = 10
score = 0

for questionNumber in range(questionsNumber):
    i=0
    numOne = random.randint(0,9)
    numTwo = random.randint(0,9)
    limit = 0
    
    while True:
        
        limit += 1
        if limit == 4:
            print('you passed the 3 tries!')
            break
        
        print('%s-calculate %s x %s :'%(questionNumber+1,numOne,numTwo))
        start = time.time()
        answer = input()
        getTime = time.time() - start
        print(getTime)
        if  getTime <= 8:
            if answer != '':
                if int(answer) in [x for x in range(0,102)]:
                    if int(answer) == numOne*numTwo:
                        print('Correct!')
                        score += 1
                        break
                    else:
                        print('Not correct!')
                        continue
                else :
                    print(f'The input must be a number,{answer} is not a Number')
                    continue
            else:
                print('Blank answers are not acceptable!')
                continue
        else:
            print('You are too late!')
            break
        
        time.sleep(1) # Add a 1-second pause
        
        start = 0
        end = 0
        
print('Score : %s/%s'%(score,questionsNumber))