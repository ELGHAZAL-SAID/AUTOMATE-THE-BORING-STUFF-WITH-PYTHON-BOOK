# MANIPULATING STRINGS



print('hello there\nhow are you?\nI\'m doing fine thanks.')
# hello there
# how are you?
# I'm doing fine thanks.

# r'' : means a row string. what inside the quotes written as it is with back slash or with ...

print(r'hello there\nhow are you?\nI\'m doing fine thanks.')

# hello there\nhow are you?\nI\'m doing fine thanks.

print('''hello guys how are you ?
        i'm fine thanks, what about you?
        i'm doing great thanks for asking
        ''')

# hello guys how are you ?
#         i'm fine thanks, what about you?
#         i'm doing great thanks for asking

"""
triple quotes can be used for 
multiline comments, like what are you reaing
now

"""

name = 'said'
# name[0] = 'f': this will cause an error  
print(name)



name = 'Joy'
age = 23

# concatenation types

print('hello my name is :'+name+'. i\'m :'+str(age)+' years old.')
print('hello my name is :%s. I am %s years old.'%(name,age))

# f-strings have an f prefix before
# the starting quotation mark
print(f'hello my name is :{name}. I am {age} years old.')


# hello my name is :Joy. i'm :23 years old.
# hello my name is :Joy. I am 23 years old.
# hello my name is :Joy. I am 23 years old.


# -----------------------string methods

# upper() : make the string in uppercase
# lower() : make the string in lowercase

print(name.upper())
# JOY


# to check if a string is in a lower or upper case we use:
#     isupper()
#     islower()

name = 'SAID'

print(name.isupper())
#True
print(name.islower())
#False

#====================== isX() functions
#the isX methods begins with the world is like "islower()" ...
#those methods return a Boolean value that describe the nature of the string

#========== Example ;
# isalpha() : if the string is consist only of letters and not blank
# isalnum() : if a string consists only of letters and numbers and not blank
# isdecimal() : if a string consists only of numeric characters and is not blank 
# isspace() : if a string consists only of spaces, tabs and newlines and in not blank
# istitle() : if a string consists only of words that begin with an uppercase letter followed by only lowercase letters

alpha = 'hellotherehowareyoudoingcheck'
alnum = '234'
decimal = '12345'
spaces = '  \n  '
titles = 'Elghazal'

print(alpha.isalpha())
print(alnum.isalnum())
print(decimal.isdecimal())
print(spaces.isspace())
print(titles.istitle())
# output:

# True
# True
# True
# True
# True


#to check if a string is starting or ending with a specific slice of string. we use:
string = 'Hello World!'
if string.startswith('Hello') and string.endswith('World!'):
    print('yes it is!')

#output:
# yes it is!


#join() and split() Methods =-------------------------------

#join() method is useful when you want to make a list items joined together in a single string:
#
listToJoin = ['Hello,','my','name','is','said']
string = ' '.join(listToJoin)
print(string)

# output

# Hello, my name is said


#split() method is used to convert a string into a list based on whitespace,tab or newline on the string in the string

otherList = string.split()
print(otherList)

# output
# ['Hello,', 'my', 'name', 'is', 'said']

#we can specify wish character to consider as the end of the string or white space or tabs split('\t') or newline split('\n') to make it a new list cellule 
# by adding what we want to specify as an argument to the method
string = 'hello@my@name@is@said'
listToHundelString = string.split('@')
print(listToHundelString)

#output:
# ['hello', 'my', 'name', 'is', 'said']

#partition Method
string = 'hello@my@name@is@'
string = string.partition('@')#split string into a tuple taking a character or symbol or ... in arg to split (note: based on the first symbol or ... it founds on the string)
print(string)
# output
# ('hello', '@', 'my@name@is@')
string = 'hello@my@name@is@'

before,sep,after = string.partition('@')
print(before,'\n',sep,'\n',after)
# output
# hello 
# @ 
# my@name@is@



#justifying text

string = 'Hello'.rjust(10) #justify to the right padded with 10 length
print(string)
string = 'Hello'.ljust(10) #justify to the light padded with 10 length
print(string)
# outpute
#      Hello
# Hello     
string = 'Hello'.rjust(10,'=') #instead of spaces we can use any symbol or character
print(string)
string = 'Hello'.ljust(10,'*') #instead of spaces we can use any symbol or character
print(string)
# output
# =====Hello
# Hello*****

string = 'Hello'.center(20) #center padded with 20 length
print(string)

# outpute
#       Hello        

string = 'Hello'.center(20,'=') #instead of spaces we can use any symbol
print(string)

# output:
# =======Hello========

#strip methods
#strip methods are used for removing whitespaces
string = '      Hello, World        '
string = string.strip()
print(string)

# output
# Hello, World

string = string.lstrip() #remove left whitespaces
print(string)
string = string.rstrip() #remove right whitespaces


string = 'Hello,World'
string = string.strip('l')#specify wish character to remove 
print(string)


# Numeric Values of Characters with the ord() and chr() Functions
string = 'A'
integer = 65
print(ord(string))
# output
# 65
print(chr(integer))
# output
# A

# copying and pasting strings with pyperclip Module

import pyperclip

pyperclip.copy('Hello, World')
print(pyperclip.paste())