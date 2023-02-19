# !python3 
# file_size_of_more_than_100MB.py => searches for exceptionally large files or folders

import os

def find_large_than_100MB_files(path,size_of_file):
    # find and list absolute paths of large files
    
    
    for root, dirs,files in os.walk(path):
        for file in files:
            file_dir = os.path.join(root,file) 
            if os.path.exists(file_dir) and os.path.getsize(file_dir) > size_of_file: #check each files it it's larger than 100MB
                print(file_dir,'|',os.path.getsize(file_dir),'bytes')


path = os.getcwd()
mb_to_bytes = 100 * 1024 * 1024 #convert 100MB to bytes

find_large_than_100MB_files(path,mb_to_bytes)

