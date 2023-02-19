import os, zipfile
from pathlib import Path

pathCwd = Path.cwd()/'organizingFiles/workOnFiles/'

#===================== compressing Files with the zipfile Module =======================


# to compress a bench of files use the zipfile module function : zipfile.zipfile()

# say, we want to discover the newFolder.zip items:

path = pathCwd/'newFolder.zip'
newFolder = zipfile.ZipFile(path)

print(newFolder.namelist()) #namelist is a zipfile module builtin function to list the name of all the items inside a zipfile (return a list of strings)

# output:
# ['newFolder/', 'newFolder/spams.txt', 'newFolder/spammers.txt']

#sat we wanna know the info about a file like its size and the size of the compressed file newFolder.zip
FileInfo = newFolder.getinfo('spams.txt')
print(FileInfo)

# <ZipInfo filename='spams.txt' filemode='-rw-rw-r--' external_attr=0x8020 file_size=0>

# to get the information from the ZipInfo object we use file_size attribute 
# before compressing
print(FileInfo.file_size)

# outPut: 0
# after compressing
print(FileInfo.compress_size)

# outPut : 0


#getting the average between before and after compression

print(f'Compressed File is {round(FileInfo.file_size/FileInfo.compress_size,2)}x smaller!')

newFolder.close()
# ============= extracting From ZIP Files ==========

path = pathCwd/'newFolder.zip'
newFolder = zipfile.ZipFile(path)

# extract all the the files from the newFolder.zip to the newFolder that we already have:
newFolder.extractall(pathCwd/'newFolder') #by giving the extractall() a path object as a arg we can specify wish folder to extract to

# extract one special file:
newFolder.extract('spams.txt',pathCwd) #extract spams.txt file from the zip file to our current working dir

newFolder.close()

# --------------------- Creating and adding to a ZIP Files --------------------------

# say we wanna compress the newFolder that we have already decompressed while a go
# to do that first we should use the ZipFile() function in the write mode ('w')
folder_To_Compress = zipfile.ZipFile(pathCwd/"newFolder/newFolder",'w')

# then we use the write() method the compress our chosen file to compress
folder_To_Compress.write('test.zip',compress_type=zipfile.ZIP_DEFLATED)
