# !python3
# compress_text_and_py_files.py -> compress test and python files only

import os, zipfile, time



def compress_python_and_text_files(folder):
    # find and compress python files or test files in a folder
    
    with zipfile.ZipFile(os.path.join(folder,'testzip.zip'),'w') as backupFilename :
        print('compressing ...')
        for foldername , subfolders, files in os.walk(folder):
            for file in files:
                if file.endswith('.txt') or file.endswith('.py'):
    
                    print(f'file {file} added to zip file {backupFilename.filename}')
                    # getting the basename folder for the files
                    basename = os.path.join(foldername,file)
                    backupFilename.write(basename, arcname=os.path.basename(basename))



path = os.path.join(os.getcwd(),'projects/quizFiles')
compress_python_and_text_files(path)