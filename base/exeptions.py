import time, sys
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(4))
print(spam(5))
print(spam(0))
print(round(spam(54),2))

def spam(divideBy):
    return 42 / divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

j = 0
while True :
    for i in range(j):
        print('*', end='')
        if i == 7:
            print('')
    j = j+1
    if j == 8:
        print('*', end='')

indent = 0
condition = True
try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
        
        
        if condition:
            indent = indent + 1
            if indent == 20:
                condition = False
        else:
            indent = indent - 1
            if indent == 0:
                condition = True
except KeyboardInterrupt:
    sys.exit()

import module sys to get the type of exception


randomList = ['a', 0,2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)

try:
    numberToget = int(input('inter a number: '))
except ValueError:
    print('you most inter an integer')


def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

while numberToget != 1:
    numberToget = collatz(numberToget)