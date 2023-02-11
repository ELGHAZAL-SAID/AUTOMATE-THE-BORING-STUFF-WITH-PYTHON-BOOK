#python3
#regexSearchInFiles.py -> search in files matching pattern entered by user

import os,re, time

path = os.path.join(os.getcwd(),'quizFiles')
def loadFiles(path,answer):
    result:list = []
    for file in os.listdir(path):
        if file.endswith('.txt'):
            with open(os.path.join(path,file),'r') as f:
                for line in f:
                    if re.search(rf'{answer}',line,re.I):
                        result.append(line)
    return result           

def talkToUser(result):
    if len(result) == 0:
        print('No result found for your pattern.')
    else:
        print('Result found'.center(20))
        for key, value in enumerate(result):
            print(key,' '*4,value)

while True:
    try:
        print('Enter the pattern you want to search for:(ctrl+c to cancel)')
        answer = input()
        print('Searching...')
        time.sleep(2)
        talkToUser(loadFiles(path,answer))
    except KeyboardInterrupt:
        print('\nuser cancelled')
        exit(1)

