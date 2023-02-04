#by using the id() function we can get the reference of a variable a list ... an object 

#mutable

spam = 45

cheese = spam


#to get the reference before the change:
print(id(spam))
    #139848488830576
print(id(cheese))
    #139848488830576

spam = 100

print(spam)
    #100
print(cheese)
    #45

#to get the reference after the change :
print(id(spam))
    #140038774345040
print(id(cheese))
    #140038774343280

# when u store a variable in to an other variable u actually store the reference of variable A in variable B,
# wish means they have the same destination to the value location in the memory

#integers are immutable, it means u can not change the value other wise u actually create a new value with a new reference
#you cAN SEE that they got deferent ids after the change


#immutable

spamList = [2,1,4,8,0]
cheeseList = spamList


cheeseList[0] = 'hello'


print(cheeseList)
#['hello', 1, 4, 8, 0]

print(spamList)
#['hello', 1, 4, 8, 0]

#to get the reference :
print(id(spamList))
    #139954921301376
print(id(cheeseList))
    #139954921301376    

# when u store a list in to an other list u actually store the same reference is the list variable <<ex : spamList>> and the list variable <<ex: cheeseList>>,
# wish means they have the same destination to the value location in the memory
#lists are immutable, it means u can change the value, that means that if u change the list value using "spamList[0]='whatever'" 
# u actually changing the list value on the memory not the reference or creating an other list  