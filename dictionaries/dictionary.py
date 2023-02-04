


birthdays = {'Mohammed':'Apr 15','Said':'Feb 2','farid':'Oct 23'}

for i in birthdays.keys():
    print(i)

for i in birthdays.values():
    print(i)
    
for i in birthdays.items():
    print(i)
# or

for k , v in birthdays.items():
    print('Key: ', k ,' Value: ', v)

name = 'Said'

if name in birthdays.keys():
    print(name,'is one of the keys in the birthdays dictionary')

# conversion the dictionary (keys, values and items(keys and values)) to a list

keysList = list(birthdays.keys())
valuesList = list (birthdays.values())
itemsList = list(birthdays.items())

print(keysList)
print(valuesList)
print(itemsList)


# check if there is the key and its value in the dictionary in the same time
# using the method get()
# get() method takes two args the first is the key of the item in the dic and the other
# is for the value to return in case the item(key and value) is not exist
sells = {'eggs':3,'potato':32,'apples':55,'tomato':7,'onion':32}

print('i booth',sells.get('eggs',0),'eggs' )
print('i booth',sells.get('milk',0),'L of milk')

# to add the key and it's value to the dictionary
# you need to check if there is the key first 
# if key not in dictionary.keys():
# to make it easy you should just use the method setdefault()

# classic way:
if 'milk' not in sells.keys():
    sells['milk'] = '2'

# easy way

sells.setdefault('milk',2)

#the first arg is for the key you want to check 
#the second arg is for the value to add in case the key is not one of the keys in the dec
#in case the key already exists the method returns the original value of dic
#in a simple way this method is for checking if a key exist or not so that you can add a value to is 

#----------------------------------------------------------
# practicingb

# check and add if not exist
while True:
    print('type your name : (black to quit)')
    choice = input()
    
    if choice == '':
        break
    name = choice[0].upper()+choice[1:].lower()
    if name in birthdays:
        print(birthdays[name]+ ' in the birthday of '+name)
        break
    elif name not in birthdays:
        print('we do not have much information bout '+name+"'s birthday")
        print('you to add this information ?, please choose yes or no') 
        choice = input()
        if choice == 'yes':
            print('Please add the birthday information :')
            birthdays[name] = input()
            print('thanks, the birthday database updated')
        else :
            break


#count number of things being brouth in a store

allGuests = {
                'Alice':{'apples':5,'pretzels':12},
                'Bob':{'ham sandwiches':3, 'apples':2},
                'Carol':{'cups':3,'apple pies':1}
            }

def countItems(guests,item):
    numberBouth = 0
    for k,v in guests.items():
        numberBouth = numberBouth + v.get(item,0)
    return numberBouth


def printAll(Data):
    print('Number of things being brouth')
    print(' - Apples          ',str(Data(allGuests, 'apples')))
    print(' - Cups            ',str(Data(allGuests, 'cups')))
    print(' - Cakes           ',str(Data(allGuests, 'cakes')))
    print(' - ham sandwiches  ',str(Data(allGuests, 'ham sandwiches')))
    print(' - Apple Pies      ',str(Data(allGuests, 'apple pies')))

printAll(countItems)

# count each litter in a string
#check and add if not exist in an other way 

message = 'i was trying to learn python long time a go and here i am trying to learn it, here it comes the time to make a new knowledge.'

characters = {}

for character in message:
    characters.setdefault(character,0)
    characters[character] = characters[character]+1    
print(characters)

#----------------------------------------------------------

# using the pprint (pretty print) can help you organize your ouput in a 
# nice way, this way :

import pprint as pp

message = 'i was trying to learn python long time a go and here i am trying to learn it, here it comes the time to make a new knowledge.'

characters = {}

for character in message:
    characters.setdefault(character,0)
    characters[character] = characters[character]+1
    
pp.pprint(characters)

# for printing the result as a string you can use pformat() mathod
print(pp.pformat(characters))



