# !python3 
# filling_Gaps.py --> locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).

import os,re



def fill_Gaps(path):

    pattern = r'^(\w+[ ]*)(\d{3,})' # pattern to find the tree nums in the file's stem

    i=1
    
    dir_content = os.listdir(path) #stor the listed files in order in a new list
    
    for file_name in sorted(dir_content):
        # extract the stem and the suffix from the file name
        stem, extension = os.path.splitext(file_name)
        
        # search for the pattern in the stem 
        match = re.search(pattern, stem)
        
        if match is not None :
            
            if not int(match.group(2)) == i: # check every file name if there is a gap
                edited_file_name = match.group(1)+str(i).zfill(3)+extension # generate new file name
                # rename the file to the edited_file_name
                os.rename(os.path.join(path,file_name), os.path.join(path, edited_file_name))                
        i += 1


fill_Gaps('Your folder path here')
