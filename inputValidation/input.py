# #input validation

# make sure that the input age is positive number
while True:
    print('Enter Your age:')
    age = input() #store the string returned by the input() function
    # use exceptions to handel the result
    try:
        age = int(age) #convert the are to an integer
    except:
        print('Please use numeric digits:') #return the warning incase the string is not a digit
        continue
    if age < 1:
        print('Please enter a positive number')
        continue
    else: #check it the age is greater than 0
        break
print(f'Your age is {age}.')

# pyinputPlus modul 

import pyinputplus as p


print(type(p))
# inputNum() function 

print('Please Enter your age:')
age = p.inputNum()
print(age)

# inputStr() function 

print('Please Enter your name:')
name = p.inputStr()
print(f'your name is {name}')

# and others 




#-------------keywords Arguments using prompt ans ...

# input a number with min value = 4 (it may equal 4)
number = p.inputNum('Enter a number:',min=4)
print(number)

# input a number with max value = 10 (it may equal 10)
number = p.inputNum('Enter a number:',max=10)
print(number)

# input a number with value lessThan 20 (number < 20)
number = p.inputNum('Enter a number:',lessThan=20)
print(number)

# input a number with value greaterThan 18 (number > 18)
number = p.inputNum('Enter a number:',greaterThan=18)
print(number)




# ========================= blank keyword Argument 

# by default blank input is not acceptable unless you use the blank keyword as an arg 
response = p.inputNum('Enter a number', blank=True)
print(response)




# ========================= limit, timeout and default keywords Args

# ============limit
# you can limit how mush time the pypi requests the user to inter the correct value in case the user inters the bad value each time 
response = p.inputNum('Enter a number', limit=3)
print(response)

# ============timeout
# you can add a timeout option to ask the user for certain amount of time.
response = p.inputNum('Enter a number', timeout=20)
print(response)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# NOTE: it the user fails to inter a valid input in the given time timeout or attempts in limit
#       it will raise exceptions RetryLimitException and TimeoutException respectively
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ========== default
# to avoid the exceptions errors, by default input will return the default value entered
response = p.inputNum('Enter a number', limit=2,default=10)
print(response)





#===============================allowRegexes and blockRegexes keyword Arguments


# ===== allowRegexes
# By adding regexes to your pypi function you will tell a pypi input what to accept and what to not
# Is is useful if you want to allow certain words or phrases to be accepted
# make the inputNum accept Roman numerals
response = p.inputNum('number: ', limit=3,allowRegexes=[r'(i|v|x|l|c|d|m)+',r'zero'])
print(response)

# ===== blockRegexes
# By adding blockRegexes to your pypi function you will tell a pypi input what to refuse 
# make the inputNum refuse certain Numbers
response = p.inputNum('number: ', limit=3,blockRegexes=[r'[082]'])
print(response)
# this wont accept the num 082 

# ============= use block and allow regexes 
# this will allow what you want and block what you need by the function 
response = p.inputStr('word: ', limit=3,allowRegexes=[r'batman',r'batwoman'],blockRegexes=[r'bat']) it will accept bat(wo)man and not bat
print(response)




# ================ passing a custom Validation function to inputCustom()
# you can create you own validation function to check what ever you want and pass it to the inputCustom() function
# as the name saying you can custom your own input

# create a function that checks if a number is odd or even
def checkOddNum(number):
    number = int(number)
    if number % 2 == 0:
        raise Exception('The digit %s is not odd.'%(number))
    return number

response = p.inputCustom(checkOddNum,limit=4,default=1)
print(response)

# =================== output 
# 22
# The digit 22 is not odd.
# jf
# invalid literal for int() with base 10: 'jf'
# 23
# 23


