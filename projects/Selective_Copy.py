#!python3
#Selective_Copy.py > select files with certain extensions and copy it to a new folder

import os,shutil

def select_files_with_extensions_and_copy_it(path,dest,extension):
    
    # walking through a dir tree and search for files with certain extensions and copy it to a new folder
    for root , dirs, files in os.walk(path):
        for file in files:
            if file.endswith(f'.{extension}'):
                shutil.copy(os.path.join(root,file), dest)
                

# path to look in for files with certain extensions
path_to_search_in = os.getcwd()
print(path_to_search_in)
# destination to copy to 
destination = os.path.join(path_to_search_in,'projects/txtfile/')

extension = 'txt'

print(f'Looking for file with .{extension} extension and copying to {destination}...')
select_files_with_extensions_and_copy_it(path_to_search_in,destination,extension)
print('Done')
