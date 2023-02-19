#!python3
#find_greatest_number_of_files_in_folder.py --> Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space


import os

def find_the_greatest_number_of_files_in_directory_tree(path):
    max_count = 0
    max_folder = None
    for root, dirs, files in os.walk(path):
        countFiles = len(files)
        if countFiles > max_count:
            max_count = countFiles
            max_folder = root
    return max_count,max_folder


path = os.getcwd()
max_count,max_folder = find_the_greatest_number_of_files_in_directory_tree(path)

print(f"The biggest files container is {max_folder}, with {max_count} files")

            