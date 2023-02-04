

# a Dictionary Data type is similar to a list however the the list 
# has [] but a Dictionary has {} and a list has index but a Dictionary 
# has a keys with different data types

# we can write a dictionary this way

myFamily = {'Father':'Farid', 'Mother':'Saadia','LittleBro':'Mohammed','BigSis':'Dounia','MiddleSis':'Fatima','littleSis':'Bouchra'}
print(myFamily)

# to print all the items in a dictionary

for i in myFamily:
    print(myFamily[i])


# Dictionaries VS lists

# -lists hav automatic way for indexing they start with 0 for the first value
# -dictionaries has no manuel way for indexing 
# -to check if two lists have a specific common value you need the same order for the both lists (list2[0] and list2[0])
# to check if tow dictionaries have the specific common value you need just to check using (Dic1 == Dic2)

# Note:     dictionaries and not ordered instead of lists 
            # a KeyError error message, much like a list’s “out-of-range” IndexError error 
            # message