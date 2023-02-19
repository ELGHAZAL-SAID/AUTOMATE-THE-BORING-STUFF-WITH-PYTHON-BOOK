#python3!
# projects/folder_that_uses_the_most_disk_space.py -> find in a dir tree the folder that uses the most disk space 




def get_folder_uses_most_disk_space(path):
    # find in a dir tree the folder that uses the most disk space 
    folderSize = 0
    folder = None
    for root , dirs ,files in os.walk(path):
        size = os.path.getsize(root)
        for r in root:
            if size > folderSize:
                folderSize = size
                folder = root
    return folderSize, folder


path = os.getcwd()
size,folder = get_folder_uses_most_disk_space(path)
print(f"the folder that uses the most disk space is {folder}, with {size} bytes")

