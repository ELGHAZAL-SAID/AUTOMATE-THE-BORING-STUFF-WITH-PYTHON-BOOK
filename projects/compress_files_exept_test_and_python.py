# !python3
# compress_text_and_py_files.py -> compress test and python files only

import os, zipfile, time



def compress_files_except_python_and_text_files(folder):
    # find and compress files except python files or test files in a folder
    
    with zipfile.ZipFile(os.path.join(folder,'testzip2.zip'),'w') as backupFilename :#open existing Zip file or create new one
        print('compressing ...')
        for foldername , subfolders, files in os.walk(folder):
            for file in files:
                if file.endswith('.txt') or file.endswith('.py'):
                    continue
                print(f'file {file} added to zip file {backupFilename.filename}')
                # getting the basename folder for the files
                basename = os.path.join(foldername,file)
                backupFilename.write(basename, arcname=os.path.basename(basename))
                print('done')


path = os.path.join(os.getcwd(),'projects/americanStyleDates')
compress_files_except_python_and_text_files(path)