#python3
#madLibs.py --> lets the user enter words in chosen words in a text

import pyinputplus as pyip
import re
from pathlib import Path


# make the list of the chosen words (ADJECTIVE, NOUN, ADVERB, or VERB)
chosen_words = ['NOUN','VERB','ADJECTIVE','ADVERB']

# getting the path of the file
path = Path.cwd()/'madlibs.txt'
patten = r'NOUN|VERB|ADJECTIVE|ADVERB'
if not path.exists(): #check if the path exists
    path.touch()

# opening the file we need the overwrite its content
with open(path,'r+') as file:
    # loading the file content
    content = file.read() #
    # getting the words that matches the pattern 
    get_Num_of_chosen_words_in_file = re.findall(patten,content)

    for i in range(len(get_Num_of_chosen_words_in_file)): #get into each word to change it
        print(content)#print the content after every change
        
        get_answer = re.search(patten, content) #look for each matched word in the content
        
        if get_answer.group() == 'ADJECTIVE': #check for the correct answer
            print('Enter an',get_answer.group().lower())
        else:
            print('Enter a',get_answer.group().lower())
        
        answer = pyip.inputStr()
        
        content = re.sub(rf'{get_Num_of_chosen_words_in_file[i]}',answer,content,count=1) #change every pattern with input value

    file.seek(0)
    
    file.write(content) #overwrite the content of the file



