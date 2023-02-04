
spam = ['apples','bananas','tofu','cats','dogs','animal']

def listTostring(lists):
    if type(lists) == list and len(lists) != 0:
        for i in range(len(lists)):
            if lists[i] == lists[-1]:
                print("and ", lists[-1])
                break
            print(spam[i]+', ', end="")


listTostring(spam)



import random

listData = []
streak = 0
streaksInRound = 0
expNumber = 0
test = 1
i = 0
for expNumber in range(10000):
    for i in range(100):
        chance = random.randint(0,1)
        if chance == 1:
            listData.append('H')
        else:
            listData.append('T')

    for i in range(len(listData)):
        if i == 0:
            pass
        
        if listData[i] == listData[i-1]:
            streak += 1
        
        else:
            streak = 0
        
        if streak == 6:
            streaksInRound +=1
            break
        
        else:
            test += 1
            continue
    listData = []
def calcChance(streak):
    return streak/ (expNumber*100)
def toPercentage(chance):
    return round(chance * 100 , 4)
print(test)
print('Chance of streak: %s%%' % toPercentage(calcChance(streaksInRound)))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end="")
    print('',sep='\n')   


tableData   =   [ 
                ['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']
                ]

def printTable(tableData):
    longestWords = []
    for list in tableData:
        longestWords.append(max(list, key=len))
    longestLen = len(max(longestWords, key=len))
    print(longestWords,longestLen)
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            print(tableData[j][i].ljust(longestLen+1), end='')
        print(' ',sep='\n')
printTable(tableData)