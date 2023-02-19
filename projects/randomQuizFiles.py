#!python3 
#randomQuizFiles.py -> generate random quiz files with random questions order

from pathlib import Path
import os,random,shelve


dbpath = Path.cwd()/'statesAndCapitals' #getting the shelve file path

# access the shelved file to get the dict of stats and their capitals
with shelve.open(dbpath,'r') as db:
        
    us_states_and_capitals = dict(db) #store the shelved file after converting it into a dictionary datatype
    #generate 35 random files
    for i in range(35):
        # generate each quiz file and it's answer in answers file
        with open(path.cwd()/'quizFiles/quizFileNum_%s.txt'%(i+1),'w') as quizFile ,open(path.cwd()/'quizFiles/answers/quizAnswersNum_%s.txt'%(i+1),'w') as answerFile:
            # building the quiz header
            quizFile.write('US state capitals\n\n'.rjust(75))
            header = 'Name:'.ljust(10)+'.............................\n\n'+'Date'.ljust(10)+'../../..\n\n'+'Period:'.ljust(10)+'............'+'\n\n'+'degree'.ljust(10)+'../50'
            quizFile.write(header)
            quizFile.write('\n\n\n')        
            
            
            # shuffle the order of the states:
            states = list(us_states_and_capitals.keys())
            random.shuffle(states) #random
            
            # generating 50 random questions
            for question in range(50):
                correctAnswer = us_states_and_capitals[states[question]]
                wrongAnswers = list(us_states_and_capitals.values())
                
                del wrongAnswers[wrongAnswers.index(correctAnswer)]
                
                answerOptions = random.sample(wrongAnswers,3) 
                answerOptions.append(correctAnswer)
                random.shuffle(answerOptions) #random
                
                # writing the question and the answer options to the quiz file.
                quizFile.write('\n\n%s - what is the capital of %s?\n'%(question+1,states[question]))
                for key, value in enumerate(answerOptions):
                    quizFile.write(chr(65+key).rjust(5)+':'.ljust(4)+value+'\n') 
                
                # writing the correct answers avery question file in the answer file
                
                answerFile.write(f"{question+1}:{chr(65+answerOptions.index(correctAnswer))}\n\n")
                