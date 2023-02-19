# shutil module (shell utilities)

import shutil as sh
import os, time, zipfile
from pathlib import Path 

path = Path.cwd()/'organizingFiles/workOnFiles/'

#---------------copying files and folders with shutil module---------------

#show the path content:
print(os.listdir(path))
# ['spam.txt', 'spams.txt']

# we can copy any file from a destination to another using shutil.copy(source,destination)

# copy spam.txt to the same path with other name:

sh.copy(path/'spam.txt',path/'newFolder')

# output : ['spam.txt', 'spams.txt', 'spammers.txt']

#--copying the hall content of the path to another folder:

# sh.copytree(path,path/'newFolder')

#========== Moving and Renaming Files and Folders ==============

# by calling shutil.move we can move a dir of file from a destination to another

#moving the spam.txt from newFolder dir to the newFolder2

if not Path(path/'newFolder2').exists(): Path(path/'newFolder2').mkdir() #make the new dir to move into ...

source = path/'newFolder/spam.txt'

sh.move(source,path/'newFolder2')
sh.move(path/'newFolder2/spam.txt',path/'newFolder2/spammers.txt')

#----------Permanently Deleting Files and Folders ----------------

# there are os module functions for deleting files and folders (empty folders) like:

# os.unlink() : for deleting file at a path
# os.rmdir() : remove only empty dirs at a path, and any files

# for avoiding empty dirs problems shutil mode provides the rmtree() function for removing files and dirs (empty or full)

# deleting all text files in the newFolder2

to_remove_from = path/'newFolder2'

for file in to_remove_from.glob('*.txt'): #delete all the fils ends with txt
    print(file)
    time.sleep(3)
    os.unlink(file)

time.sleep(5)
sh.rmtree(to_remove_from) #delete the dir at the path to_remove_from

#====== safe Deletes with send2trash module============

# fo keeping what you deleted by mistake in the trash so that you can restore it you should use send2trash module

# to install it use : pip install --user send2trash

# how to use :
    # import send2trash
    # send2trash.send2trash(to_remove_from/'spam.txt') #move spam.txt from newFolder2 to recycle bin (trash)


#------------ Walking a dir tree ========

# to make a change (rename, open ...) on a folder and its items (file or subfolder) you gotta use the builtin os function : os.walk()

# lets print every ,folder,subfolder and file in the workOnFiles dir:
import os
for mainFolder,subFolders,files in os.walk(path):
    print('The folder name:'+mainFolder)
    
    for  subFolder in subFolders:
        print('subFolder of '+mainFolder+' is :'+subFolder)
    
    for file in files:
        print('File inside '+mainFolder+' is: '+ file)
    
    print('')

# the main work os.walk() function do is :
#     return tree values in each iteration:
#         -> a string of the current working dir (parameter path you gave to the function) name
#         -> a list of strings of the subFolders inside the cwd 
#         -> a list of string of files inside the cwd





