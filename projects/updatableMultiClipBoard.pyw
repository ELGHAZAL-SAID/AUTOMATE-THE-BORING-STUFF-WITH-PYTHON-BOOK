#! python3
#mclip.py - A multi-clipboard program.
#usage:
    # py.sh mcb.pyw save <keyword> - Saves clipboard to keyword.
    # py.sh mcb.pyw <keyword> - Loads keyword to clipboard.
    # py.sh mcb.pyw list - Loads all keywords to clipboard.

import subprocess,shelve,os
import sys, pyperclip,pprint


# creating the shelve file (tha database to store and restore the data)
with shelve.open('/home/username/clipBoard/dbClip') as file:
    
    # checking the args
    if len(sys.argv)<2:
        print('Usage: python mclip.py [Keyphrase] - copy phrase text\npy.sh mcb.pyw save <keyword> - Saves clipboard to keyword.\npy.sh mcb.pyw <keyword> - Loads keyword to clipboard\npy.sh mcb.pyw list - Loads all keywords to clipboard\npy.sh mcb.pyw remove key - remove a keywords from clipboard\npy.sh mcb.pyw clean - clean all the clip clipboard')
        exit()
    # save the key and the value
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        if sys.argv[2].lower() in file.keys():
            print('The keyphrase %s is already exists in the clipboard'%(sys.argv[2]))
        else:
            file[sys.argv[2].lower()] = pyperclip.paste().lower()
            print('The keyphrase "%s" is saved in the clipboard'%(sys.argv[2]))
    # remove chosen key from the clipboard db
    elif len(sys.argv) == 3 and sys.argv[1].lower() =='remove':
        if sys.argv[2].lower() in file.keys():
            del file[sys.argv[2].lower()]
            print('The keyphrase "%s" is removed from the clipboard'%(sys.argv[2]))
        else: 
            print('the key "%s" is not in the clipboard, you can check using list key.'%(sys.argv[2]))
    
    # incase there is only 2 agrs
    elif len(sys.argv) == 2:
        keyphrase = sys.argv[1] #first command line arg is the keyphrase
        # list the content of the clipboard db 
        if keyphrase.lower() == 'list':
            if len(file) == 0 :
                print('List is empty')
            else:
                for key , value in file.items():
                    print(key.ljust(len(max(file.keys(),key=len))),":",value,'\n')
                    
        # clean the clipboard db
        elif sys.argv[1].lower() == 'clean':
            if len(file) == 0 :
                print('No data to clean')
            else:
                file.clear()
                print('Cleaned')    
        # otherwise copy the value of he key given to the clipboard
        elif keyphrase in file.keys():
            pyperclip.copy(file[keyphrase])
            print('Text for '+keyphrase+' copied to clipboard')
        else:
            print('There is no text for '+keyphrase)
    elif len(sys.argv) > 3:
        print('Wrong option, check the usage above and try again')



