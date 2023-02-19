#python3
#Renaming Files with American-Style Dates to European-Style Dates

from pathlib import Path
import re,os, random,time
import shutil as sh

pattern_style_date =    r'''^(.*?)             #all the text before the date
                            ((0|1)\d)-         #first 2 digits
                            ((0|1|2|3)\d)-     #second 2 digits
                            ((19|20)\d{2})        #last 4 digits
                            (.*?)$             #incase there or there isn't an extension 
                            '''

# def look_for_american_style_dates():
#     with open
path = Path.cwd()/'projects/americanStyleDates/'


def generate_files_with_american_date_style(path,number_of_files): #generate a bunch of files named with american date style 'MM/DD/YYYY'
    # loop for the number given to open the files
    for i in range(number_of_files):
        mount = random.randint(1,12) #random mounts
        day = random.randint(1,31)   #random day
        year = '%s%s'%(random.randint(19,20),str(i).zfill(2)) #random day
        with open(path/f'{str(mount).zfill(2)}-{str(day).zfill(2)}-{year}.txt','w') as f:
            print('')
    print('Done')

def delete_all_the_text_files(path):
    # delete all the files from the path
    while len(os.listdir(path)) > 0 : #while the dir is not empty
        os.unlink(path/f'{os.listdir(path)[0]}')

def rename_files_w_us_style_date_with_european_style_date(path):
    # open every file from a specific path
    for i in range(len(os.listdir(path))):
        
        with open(path/f'{os.listdir(path)[i]}') as file:
            # store every file's name that matches the pattern
            matched_us_date = re.search(pattern_style_date,file.name,re.VERBOSE)
            
            if matched_us_date == None: #continue looping if the match dose not exists
                continue
            # store every part in a different variable using groups 
            before = matched_us_date.group(1) # what is after the date 
            mount  = matched_us_date.group(2) # the date in us_style 
            day    = matched_us_date.group(4) # the mount in us_style
            year   = matched_us_date.group(6) # the year in us_style
            after  = matched_us_date.group(8) # what is before the date
            
            # generate the european style date 
            euro_style_date_file_name = before+day+'-'+mount+'-'+year+after
            
            # getting every file path (us style)
            us_file_name = path/f'{os.listdir(path)[i]}'
            
            # generate the european style date file path
            euro_file_name = path/euro_style_date_file_name
            
            # checking if the programe is working 
            print('renaming',os.listdir(path)[i],'to:',euro_style_date_file_name,'...')
            
            #renaming each file with the new name made
            sh.move(us_file_name,euro_file_name)




# generate files if dir empty
if not len(os.listdir(path)) > 0:
    generate_files_with_american_date_style(path,3
                                            0)

rename_files_w_us_style_date_with_european_style_date(path)

delete_all_the_text_files(path)