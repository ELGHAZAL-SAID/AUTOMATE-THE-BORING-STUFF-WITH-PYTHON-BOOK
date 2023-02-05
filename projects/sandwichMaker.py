#!python3
#sandwichMaker.py -> asks user to chose his sandwich preferences using 

import pyinputplus as pypi

# choice lists => user sandwich preferences

breadType = ['wheat','white','sourdough']
proteinType = ['chicken','turkey','ham','tofu']
cheeseType = ['cheddar','Swiss','mozzarella']
additionalItems = ['mayo','mustard','lettuce','tomato']
price = 0
choiceList = []


# facture printing function 

def facture(sandwichNum,choiceList,price):
    print('Your order:')
    print('sandwich:'.ljust(20),'items'.center(20),'price'.rjust(30))
    for sandwich in range(sandwichNum):
        print('sandwich'+str(sandwich+1).ljust(10),'/'.join([item for item in choiceList]).center(20),str(price).rjust(25))
    print('total :'.ljust(10),price*sandwichNum)

print('Hello to sandwich Ahmad')
# -----------ask the user about the bread type
try:
    choice = pypi.inputMenu(prompt = 'What type of bread would you like to add:\n',numbered=True, choices=breadType, timeout=90,default=breadType[0])
    if choice in breadType:
        choiceList.append(choice)
        choice = ''
        price += 1
except pypi.timeoutException:
    print(f'You took too long to choose, we will have to choose for you the {breadType[0]} Bread type')

# ask the user about the protein type

try:
    choice = pypi.inputMenu(prompt = 'What type of Protein Type would you like to add:\n',numbered=True, choices=proteinType, timeout=90,default=proteinType[0])
    if choice in proteinType:
        choiceList.append(choice)
        choice = ''
        price += 3
except pypi.timeoutException:
    print(f'You took too long to choose, we will have to choose for you the {proteinType[0]} as a protein type')

# give options to the user to choose the cheese and additional items (by using inputYesNo)

try:    
    answer = pypi.inputYesNo(prompt = 'do you want to add cheese (yes/no or 1/0):\n',allowRegexes=[(r'(y|yep|y|YES|n|nop|NO|N|1|0)+')],timeout=90,default='No')
    if answer == 'yes'or answer == 'YES' or answer == 'yep' or answer == '1' or answer == 'y':
        # ask the user to choose cheese type
        try:
            choice = pypi.inputMenu(prompt = 'What type of cheese would you like to add:\n',numbered=True, choices=cheeseType, timeout=90,default=cheeseType[0])
            if choice in cheeseType:
                choiceList.append(choice)
                choice = ''
                price +=2
        except pypi.timeoutException:
            print(f'You took too long to choose, we will have to choose for you the {cheeseType[0]} choice')
except pypi.timeoutException:
    print(f'You took too long to choose, we will take it as "NO"')

try:
    answer = pypi.inputYesNo(prompt = 'do you want to add additional items:\n',allowRegexes=[(r'(y|yep|y|YES|n|nop|NO|N|1|0)+')],timeout=90,default='No')
    if answer == 'yes'or answer == 'YES' or answer == 'yep' or answer == '1' or answer == 'y':
        # ask the user to choose the additional item
        try:
            choice = pypi.inputMenu(prompt = 'What type of additional items would you like to choose:\n',numbered=True,choices=additionalItems,timeout=90,default=additionalItems[0])        
            if choice in additionalItems:
                choiceList.append(choice)
                choice = ''
                price += 1
        except pypi.timeoutException:
            print(f'You took too long to choose, we will have to choose for you the {additionalItems[0]} choice')
except pypi.timeoutException:
    print('You took too long to choose, we will take it as "NO"')

# ask the user about the quantity 
try:
    sandwichNum = pypi.inputInt('Enter how many sandwiches you want to order (one by default):',blockRegexes=[r'^[0]'],timeout=90,default=1)
except pypi.timeoutException:
    print('you took too mush time, one sandwich is selected')

# print the final result for the users
facture(sandwichNum,choiceList,price)