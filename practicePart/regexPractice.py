# re.compile

# r''

# search method returns a an object of the first match found in a given string

# getting the actual matches string by using the group() method to return a string

# group 0 covers the hall matched string 
# group 1 matches the first part of the string matched by the regex 
# group 2 matches the second part of the string matched form the regex

# you can use the backslash \) or \( or \. to escape its functionality in the regex or you can yous the braces []

# if there is no groups it will return a string else if there is a group or more in the regex it will return a list of tuples based on how mush group is existed

# in a regex expression a '|' means OR

# The '?' symbol can  be used in two things, first in a non-greedy like {1.4}? or in optional selection \d?

# the difference between + and * is that + goes for one or more regex in the other hand * goes for rezo or more

# {3} means the length is constant and fixed in 3 but {3,5} means that there is a range from 3 to 5 based on number of regexes matches in the string given 

# \d meand digits
# \w means word (letter, digit, _)
# \s means spaces (spaces tabs newlines)

# \D means non-digits
# \W means non-words
# \S means non-spaces

# the difference between .* and .*? is that .* means zero or more eny character (includes newlines cause * presents zero also so newlines will be included) but .*? means zero or one (any character including newlines)

# [a-z1-9]

# regex = re.compile(r'',r.I) by adding the arg re.I or re.IGNORECASE 

# . matches all the characters except newlines, it will match all the characters including newlines

# it will return X drummers, X pipers,five rings, X hens

# it allows you to add comment and newlines inside the compile method

# import re
# pattern = r'(\d{1,3})(,\d{3})(.\d+)?'
# matches = re.findall(pattern,"This string contains numbers like 1,545, 5,212,565, and 454,453,632. It also has decimal numbers like 1,545.123 and 5,212,565.456." )
# match = [''.join(match) for match in matches]
# print(' '.join(match))

# pattern = r'[A-Z][a-z]+\sWatanbe'

# pattern = r'(alice|bob|carol)\s(eats|pets|throus)\s(apples|cats|baseballs\.)',re.I
