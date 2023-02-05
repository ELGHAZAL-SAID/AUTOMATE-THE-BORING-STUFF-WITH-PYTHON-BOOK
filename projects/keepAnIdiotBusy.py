#!python3
#keepAnIdiotBusy -> how to keep an Idiot busy for hours

import pyinputplus as pypi


while(True):
    print('Do you know how to keep an idiot busy for hours: ')
    answer = pypi.inputYesNo(allowRegexes=[r'n|y|yep|nop'])
    if answer == 'no' or answer == 'n' or answer == 'nop':
        break
    else:
        print('Ok, let\'s do it!')
        answer = pypi.inputYesNo('are you sure you want to know (type yes/no): \n',allowRegexes=[r'n|y|yep|nop'])
        if answer == 'yes':
            continue
