#python3
#readWriteFiles.py -> read and write plaintext files

from pathlib import Path
# ------------------ reading a text files content using read_text() function and write a new file or overwrite an existing one by using the write_file() form the Path object ------------------
path = Path('/home/username/Desktop/randomFiles/test')

if path.exists() and path.is_file(): #check if the path exist and ends with a file
    #reading the text files content
    content = path.read_text(encoding="utf-8") # read
    print(content)
    #overwriting the existing file with the new content
    content = path.write_text('checking if this will be overwrite the file or not!')
    print(content)
else:
    print("File does not exist")

# Opning and closing files uding open() and close() functions
path2 = Path('/home/username/Desktop/randomFiles/test2')
file = open(path2,'r')
if file:
    print('opened')
    # reading the file content
    print(file.read()) #reading the hall file content
    file.seek(0) #replacing the pointer to the beginning of the file
    print(file.readlines()) #reading files by lines
else:
    print('file have not been opened')
file.close() #clode


# =============writing a file
path3 = Path('/home/username/Desktop/randomFiles/test3')
file = open(path3,'w+') #writing plus option to overwrite the file
if file:
    file.write('this is the new text added to the file\n') # since open has write option when we use read we overwrite the actual file         
    file.seek(0)  
    content = file.read() #read the file content
    print(content)
file.close() #close the file


# create and write a file if not exist using open() and write() methods
path = Path('/home/username/Desktop/randomFiles/test4')

file= open(path,'w+') #opening the file if it doesn't exist
file.write('this is the new text added to new created file\n')
file.seek(0)
print(file.read())

# Note:
    # when using open(path) ... file.close. you are the responsible to handle errors if u forgot to close the from django.utils.translation import ugettext_lazy as 
    # but by using the : with open(path) as file: ... the python handles errors and close the file automaticly when the with block is finished 

# ===========================shelve Module and saving variables 
# importing shelve module
# shelve file can be treated as a database to store objects or data or variables to it and load it later
import shelve,pprint
# opening the shelve file 
info: dict = {'name':'joy', 'age':22,'email':'test@example.com','password':'***********'}
with shelve.open('./myDb') as file:
    file.update(info) #update the database information
    print(pprint.pformat(dict(file))) #print the content of the file by converting it to a dictionary datatype and print it in a readable way using pprint.pformat()

# output:
    # {'age': 22,
    #  'cats': ['Zo', 'Pooka', 'Simon'],
    #  'email': 'test@example.com',
    #  'name': 'joy',
    #  'password': '***********'}
