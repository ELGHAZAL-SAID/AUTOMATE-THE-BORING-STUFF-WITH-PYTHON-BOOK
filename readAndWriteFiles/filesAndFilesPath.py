#!python3 
#filesAndFilesPath.py -> dealing with files and it's paths

#backslash and Forward Slash
# for windows : backslash = \
# for macOs and linux : forwardSlash = /
# to handel both options you need to use the pathlib module method path()

from pathlib import Path
import os
from os import path

#for example we want to detect the path home/files/python or home\files\python
path = Path('home','files','python')
print(path)
# in my case i use linux so the output will be: home/files/python

filesNames = ['file.txt','file.sh','file.dot','file.json','file.csv']
path = '/home/user/Desktop'
for fileName in filesNames:
    print(Path(path,fileName))

# outPut:
# /home/user/Desktop/file.txt
# /home/user/Desktop/file.sh
# /home/user/Desktop/file.dot
# /home/user/Desktop/file.json
# /home/user/Desktop/file.csv

#--------- Using '/' operator to join paths

path1 = Path('spam')/'bacon'/'eggs'
# or
path2 = Path('spam') / Path('bacon','eggs')

print(path1)
print(path2)
#spam/bacon/eggs
#spam/bacon/eggs

#----- using / to concatenate the paths is more safe and use full instead of the '+'

# ------------------------------The current working Directory

# to change the current directory (the place you launch the python script not the file location itself) you should use the function os.chdir(newPath)
 
# to ger the current directory path you should use the function Path.cwd()
print(Path.cwd())
# output: /home/UserName/Desktop/Files/Get_python3
os.chdir('/home/UserName/Desktop')
print(Path.cwd())
# output: /home/userName/Desktop

print(os.getcwd())

# =================getting the home dire path
print(Path.home())

#---------------------- Absolute vs Relative Paths

# Absolute : begins with the root dir (/ for linux)
# Relative : starts with the program currents dir




#create a dir using the os.makedirs() and Path().mkdir()

# the makedirs() create dirs if not exists and also create child lis a/b/c ...

os.makedirs('myFiles')

# the Path().mkdir() create a dir fir not exists and dose not support the child creation unless you add the key word parents=True
Path('myFiles/test/spam/iamHere').mkdir(parents=True)

# delete a full dir :
from shutil import rmtree
rmtree('myFiles')

# ------------ handling absolute and relative paths

# checking if a path is absolute or relative using is_absolute()

path = Path.cwd().is_absolute() 
if path:
    print(Path.cwd())
else:
    print('it is not absolute')


#---------------------in os module there is :
os.path.isabs(path)  # to check if the path is absolute

print(os.path.relpath('/home/username/Desktop/Files/','Desktop')) # returns a string of a relative path form the start (agr 2) of the path, if the start is missing it will use the current dir as a start path
# output
#     ../../..
print(os.path.abspath('readAndWriteFiles/readWritefiles.py'))
# output:
# /home/username/Desktop/Files/Get_python3/readWriteFiles/readWriteFiles.py


# you can get the absolute path from a relative path

relativePath = Path('text')

absolutePath = Path.cwd() / relativePath
print(os.path.join(absolutePath, relativePath))
print(absolutePath)

# output : 
# /home/userName/Desktop/Files/Get_python3/test/makepython3/files

# using os functions like :
path3 = os.path.abspath(relativePath)
print(path3)
# output : 
# /home/userName/Desktop/Files/Get_python3/test/makepython3/files


#=========== getting the part of a file path with pathlib =========

# extract the anchor (c drive or d drive in windows) in linux or macos:
path = Path('/home/username/Desktop/files/python/readWriteFiles/readWriteFile.py')
print(path.anchor)
# /
#extract parent of the file:
print(path.parent)
# /home/username/Desktop/files/python/readWriteFiles/
# extract name of the file:
print(path.name)
# readWriteFile.py
# extract stem of the file
print(path.stem)
# readWriteFile
# extract extension:
print(path.suffix)
# .py

# both .name and .suffix and .anchor (.drive) returns the same data type <string>
# the .parent returns a Path object
# patents attribute (it is the not parent) can access to any parent using an integer:

for i in range(len(Path('/home/username/Desktop/files/python/readWriteFiles/readWriteFile.py').parents)):
    print( Path('/home/username/Desktop/files/python/readWriteFiles/readWriteFile.py').parents[i])

# output:
# /home/username/Desktop/files/python/readWriteFiles
# /home/username/Desktop/files/python
# /home/username/Desktop/files
# /home/username/Desktop
# /home/username
# /home
# /

#-------------os module getting Paths parts --------------------------------

path = '/home/username/Desktop/files/python/readWriteFiles/readWriteFiles.py'

# for os module there is just tow parts in a pth (Dir name and Base name)

dirname = os.path.dirname(path)
basename = os.path.basename(path)
print(dirname,'\n', basename)
# output :
# /home/username/Desktop/files/python/readWriteFiles 
# readWriteFiles.py

# Note: to separate directories and file name.ext from each other use:

print(os.path.split(path))
# output is a tuple (dirname, basename):
# output:


# getting parts of the path using the os.sep function, it returs a list of strings of each for folder in the path and the file name also

print(path.split(os.sep))
# output:
# ['', 'home', 'username', 'Desktop', 'files', 'python', 'readWriteFiles', 'readWriteFiles.py']


#---------------------------------finding files sizes and folder contents-------------------------------

# for getting size of a file or folder (empty or full) in bytes in a path:

path = os.getcwd()
print(path)

# to list files and dirs inside a current folder, it's helpful to use the listdir function from the os module os.listdir()
list = os.listdir(path)
print(list)
print(os)
# output:
# ['modules', 'projects', '.git', 'stringManipulating', 'practicePart', 'raquirements.txt', 'regexes', '.vscode', 'lists&tuples', 'functions', 'dictionaries', 'inputValidation', 'base', 'readAndWriteFiles']

# to get total size of a current folder in bytes, it will be easy to combine the os.getsize() and os.listdir() functions
totalSize = 0

for file in list:
    totalSize += os.path.getsize(os.path.join(path, file))
print(totalSize)


#======== Modifying a list of files Using Global patterns

p = pathlib.Path('/home/username/Desktop/Files/pdfFolder')
list = list(p.glob('*.pdf'))
print(list,'\n')
#note : you can add the ? symbol to the end or beginning of the pattern to tell python to take one and only any character (?x? for exe or txt or ...)
# listing the results
for path in list:
    print(path)



#-------------- checking if the path is valid or not ----------------
# to check it a path is valid by checking is the folder or the file is exists or not:

path = Path('/home/username/Desktop/')
if path.exists():
    print('Path %s is exists'%(path))
else:
    print('Path %s is not exists'%(path))
# output :
#     Path /home/username/Desktop is not exists

# you can check if a file or dir exists or not by using the is_file() and is_dir() functions:
path = Path('/home/username/Desktop/Files/pdfFolder/')
if path.is_file():
    print('the %s is a file'%(path.name))
elif path.is_dir():
    print('the path %s ends with a directory'%(path))
# Note:
# all of the above about the exists() and is_dir() also is_file() functions are been provided by the Path object 
# the os module has his own fuctins like : os.path.exists() and os.path.isfile() also there is os.path.isdir() functions.
