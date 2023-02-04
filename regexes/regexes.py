import re  #regular expressions module 

# checking decimal number Regex

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

answer = phoneNumRegex.search('My number is 555-532-3265.')

print('Phone number found:', answer.group(1),answer.group(2))

print('Phone number found:', answer.group())

# checking decimal with parentheses ()

PhoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d)')
answer = PhoneNumRegex.search('My phone number is (245) 555-512-5019.')
print('Phone number found:',answer.group(1),answer.group(2))

# combine both in one(\(\d\d\d\))

phoneNumRegex = re.compile(r'(\d\d\d-|\(\d\d\d\))(\d\d\d-\d\d\d\d)')

answer = phoneNumRegex.search('My number is (555)532-3265.')

print('Phone number found:', answer.groups())




# optional text in a Regex with '?' <zero or one>

batRegex = re.compile(r'Bat(wo)?man')
answer = batRegex.search('The adventure of Batman')
print(answer.group(0))
answer = batRegex.search('The adventure of Batwoman')
print(answer.group(0))

# try it with a phone number:
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
answer = phoneNumRegex.search('My number is 555-532-3265.')
print(answer.group())



# optional multi words with star * <match one or more> 

batRegex = re.compile(r'Bat(wo)*man')

answer = batRegex.search('The adventure of Batman')
print(answer.group(0))

answer = batRegex.search('The adventure of Batwoman')
print(answer.group(0))

answer = batRegex.search('The adventure of Batwowowowowowowowowoman')
print(answer.group(0))



# optional multi words with plus + <match one or more>  

batRegex = re.compile(r'Bat(wo)+man')

answer = batRegex.search('The adventure of Batman')
if answer == None:
    print('none')

answer = batRegex.search('The adventure of Batwoman')
print(answer.group(0))

answer = batRegex.search('The adventure of Batwowowowowowowowowoman')
print(answer.group(0))



# matching specific repetitions with Braces '{}':

haRegex = re.compile(r'(Ha){3}')
answer = haRegex.search('HaHaHa')
print(answer.group())

# (ha){3} : (ha)(ha)(ha) -> hahaha
# (ha){2,4}: (ha)(ha) or (ha)(ha)(ha) or (ha)(ha)(ha)(ha)
# (ha){,3} : (ha) or (ha)(ha) or (ha)(ha)(ha)
# (ha){3,} : (ha)(ha)(ha) or (ha)(ha)(ha)(ha) or ... 



# greedy and non-greedy matching using "?" <lazy greedy>:

greedyRegex = re.compile(r'(Ha){3,9}') #here it will get the longest possible slice in the given string
answer = greedyRegex.search('HaHaHaHaHaHaHaHa')
print(answer.group())

# output:
#     HaHaHaHaHaHaHaHa


nonGreedyRegex = re.compile(r'(Ha){3,9}?') #here it will get the shortest possible slice in the given string
answer = nonGreedyRegex.search('HaHaHaHaHaHaHaHa')
print(answer.group())

# output:
#     HaHaHa



# search vs findall methods
# search : returns the first matching in the searched string
# findall : returns a LIST of all the matching strings in the searched string as long as there is no groups in the Regex
# if so it will return a list of tuples 

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
answerWithSearch = phoneNumRegex.search('Cells: 415-555-9999 work:212-555-0000')
answerWithFindall = phoneNumRegex.findall('Cells: 415-555-9999 work:212-555-0000') 

print(answerWithSearch.group())
print(answerWithFindall)

# output:

# 415-555-9999
# [('415', '555', '9999'), ('212', '555', '0000')]


# ===========shorthands code characters class:
# \d : numeric only
# \D : not Numeric only
# \w : words (letters, nums, spaces, underscores, ...) only
# \W : not words only
# \s : spaces only (space, tab, new line, )
# \S : not words only

# Making special class for your own 

# example class : [a-zA-Z1-9] is a class including only letters (upper and lower) and numbers

vowelRegex = re.compile('[aeiouAEIOU]') #only vowels class
answer =  vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(answer) #prints all the vowels in the string as a list
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

#-------------------negative class
# negative class = [^aeiouAEIOU] is used to match all the characters that are not in the class

consonantRegex = re.compile(r'[^aeiouAEIOU]') #ALL letters except vowels
answer =  consonantRegex.findall('RoboCop eats baby food. BABY FOOD')
print(answer) #prints all the consonants in the string as a list
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D']

# -----------Caret and Dollar Sign characters:
# ^ : used also in the beginning of an expression to indicate that match must occur at the beginning of searched list
#$  : used also in the end of and expression to do the inverse if the '^'


string = 'Hello , i am john and i am 23 years old, bye'

beginsWithHello = re.compile(r'^Hello') #starts with Hello
endsWithBye = re.compile(r'bye(.)?$') #end with bye
answer = beginsWithHello.search(string)
print(answer.group()) #prints
answer = endsWithBye.search(string)
print(answer.group()) #prints



#-------------------------------- the wildcard character ot the dot (.):

# the wildcard or the dot (.) : used to match any character except for newlines
atRegex = re.compile(r'.at') # bring every character followed by at
answer = atRegex.findall('The cat in the hat sat on the flat mat, cached by medmat.')
print(answer) #prints
# ['cat', 'hat', 'sat', 'lat', 'mat', 'mat']


# dot star (.*) used to match every(eny)thing

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
answer = nameRegex.findall('First Name: Said Last Name: ELGHAZAL')
print(answer)
# ['Said', 'ELGHAZAL']

# dot star (.*?) used to match every(eny)thing in a non-greedy way (match less characters possible) after the dot 

nonGreedyRegex = re.compile(r'<.*?>')
answer = nonGreedyRegex.findall('<To serve man> for dinner.>')
print(answer)
# ['<To serve man>']

GreedyRegex = re.compile(r'<.*>')
answer = GreedyRegex.findall('<To serve man> for dinner.>')
print(answer)

# ['<To serve man> for dinner.>']

# to force matching newlines in the wildcard (dot character) we add one ome agr to the compile method
# wish is "re.DOTALL"

newLineRegex = re.compile(r'.*', re.DOTALL)
NonNewLineRegex = re.compile(r'.*')

answer = NonNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(answer.group())
# Serve the public trust.

answer = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(answer.group())
# Serve the public trust.
# Protect the innocent.
# Uphold the law.



# insensitive matching using re.I or re.IGNORECASE args in compile method

roboCop = re.compile(r'robocop', re.I)
answer =  roboCop.search('RoboCop is peat man, part machine, all cop.')
print(answer.group())

# else 

roboCop = re.compile(r'robocop')
answer =  roboCop.search('RoboCop is peat man, part machine, all cop.')
if answer:
    print('Accepted')
else :
    print('declined')

# declined


#======================substituting Strings with the sub() Method:
# sub() Method is used to replace matched string with a given string (so it takes to args)

nameRegex = re.compile(r'Agent \w+')
answer = nameRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent.')
print(answer)

# show the first letter of a word 

agentNameRegex = re.compile(r'Agent (\w)\w*')
answer = agentNameRegex.sub(r'\1****',"Agent Alice told Agent Eve knew Agent Bob Was A double agent.")
print(answer)

# comment Regex and ignore commenting inside the compile function using re.VERBOSE

# before
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# after

phoneRegex = re.compile(r'''
                        (\d{3}|\(\d{3}\))?              # area code
                        (\s|-|\.)?                      # separator
                        \d{3}                           # first 3 digits
                        (\s|-|\.)                       # separator
                        \d{4}                           # last 4 digits
                        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
                        )''', re.VERBOSE)






