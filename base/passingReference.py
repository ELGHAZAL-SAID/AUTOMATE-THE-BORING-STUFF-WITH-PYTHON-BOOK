#passing references
import copy as cp


def eggs(someParameter):
    someParameter.append('hello')
    print(id(someParameter))


spam = [1,2,3,4]

eggs(spam)

print(spam)


# The copy Module’s copy() and deepcopy() Functions

spam = [1,2,3,4,5,6,7]
print(id(spam))

cheese = cp.copy(spam)
print(id(cheese))

cheese[0] = "Hello"

print(spam)
print(cheese)




listOflists =[
                [1,2,3,4],
                ['hello',"world"],
                ['said','khalid','Mohamad','test']
            ]

listTwo = cp.deepcopy(listOflists)

listTwo[0][1] = 'test trying'

print(listOflists[0:])

print(listTwo[0:])
