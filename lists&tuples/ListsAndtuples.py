

listOfnames = ['said','simo','farid','amjad']    #names list

for i in listOfnames:   #print list content in order
    print(i)

for i in range(1,len(listOfnames)+1): #print list in disorder
    print(listOfnames[-i])


if 'said' in listOfnames:   #check if a string in the list
    print('it is there')

print(listOfnames[0:3])  #print a slice pf a list from index 0 to length 3
    #['said', 'simo', 'farid']

print(listOfnames*2)       #replication of a list 'list * i'// i is an integer
    #['said', 'simo', 'farid', 'amjad', 'said', 'simo', 'farid', 'amjad']
print(listOfnames+listOfnames)      #concatenate two list 'list + list' // + is a concatenation operator  
        #['said', 'simo', 'farid', 'amjad', 'said', 'simo', 'farid', 'amjad']

del listOfnames[0] # removing a value listOfnames[0] from the list using the key word 'del' 
print(listOfnames)  
    # ['simo', 'farid', 'amjad']  'list values except "said" '


cities = []
citiesNumber  = int(input('Number of cities you want to enter : '))

while True:

    names = input('inter a city '+str(len(cities)+1) +' name : ')
    if names == '':
        print('inter a valid string')
        continue
    # cities = cities + [names]         #traditional way that concatenate the cities list and the [names] value
    cities.append(names)        #append() function adds a passed value to is to the <<<<"end">>> cities list
    #cities.insert(0,names)        # we can use insert() function to add values by adding the <<<<<index>>>> where we want to store and then the ????"value"??? 
    if citiesNumber == len(cities):
        break
print(cities)

pitsList = ['katy','tome','rosalinda','white','robin']

pitName = input('inter the name you want to check if exist: ')

if pitName not in pitsList:    # 'in' and 'not in' operators checks if the input is "in" or 'not in' the list       
    print(pitName+' is not exist in the pits list.')
else:
    print('here it is!!! '+pitName+' is existed in the pits list')


import random

pitsType = ['dog','cat','rabbit']
# print(type(pitsType))
print(pitsType.index('dog')) #index() Method returns the index of a passed value if exist in the list

typeOne,typeTwo,typeTree = pitsType  #The multiple assignment trick (technically called tuple unpacking) is a shortcut that lets you assign multiple variables with the values in a list in one line of code
#in order the first variable will take the first value in the list an so on...
print(typeOne)
print(typeTwo)
print(typeTree)
    #output:    #dog
                #cat
                #rabbit


for index, item in enumerate(pitsType): #enumerate function separate the index and the value of each item in the list and stor it in 'index' and 'item' (for loop variables)
    print('index ' + str(index) + ' Pit type is ' + item )

random.shuffle(pitsType)    #This method changes the original list, it does not return a new list.
print(pitsType)    #['dog', 'rabbit', 'cat'] instead of  ['dog','cat','rabbit']


pitsType.append('names')#append() function adds a passed value to is to the <<<<"end">>> pitsType list

#pitsType.insert(0,"names")        # we can use insert() function to add values by adding the <<<<<index>>>> where we want to store and then the ????"value"??? 

pitsType.remove('dog')  # The remove() method gets the value to be removed from the list it is called 

# index = 0
#

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort() # sorting the values of spam in alphabetic order
    #output : ['ants', 'badgers', 'cats', 'dogs', 'elephants']
spam.sort(reverse=True) #sorting values in disorder by adding the argument reverse=True
    #output : ['elephants', 'dogs', 'cats', 'badgers', 'ants']
    
    # <<note>> sort() dose not sort list with different values like spam = [1, 3, 2, 4, 'Alice', 'Bob']


spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort(key=str.lower) # sort() uses "ASCIIbetical order", it means it will give priority to the uppercase letters than lowercase letters rather than alphabetic order

spam = ['cat', 'dog', 'moose']
spam.reverse()  # reverse list items order
    #output : ['moose', 'dog', 'cat']



tupleDatatype = (3,5,7,'said','i am here')  # tuple syntax, tuples are immutable  like strings

for i, item in enumerate(tupleDatatype):
    print('index :',i,' data :',item)
    

a = [1,2,3,4,5,6,7]
b = ['said',"test",1]

for index_1 , index_2 in zip(a, b):
    print(a, b)