#English to pit latin

print('Enter the English message to translate into pig latin:')
message = input()

vowels = ('a','e','i','o','u','y')

piglatin = []

for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        piglatin.append(prefixNonLetters)
        continue
    suffixNonLitters = ''
    while not word[-1].isalpha():
        suffixNonLitters += word[-1]
        word = word[-1]
    
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    word = word.lower()
    
    prefixConsonant = ''
    while len(word) > 0 and not word[0] in vowels:
        prefixConsonant += word[0]
        word = word[1:]
    if prefixConsonant != '' :
        word += prefixConsonant +'ay'
    else :
        word += 'yay'
        
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    piglatin.append(prefixNonLetters + word + suffixNonLitters)    
print(' '.join(piglatin))

string = 'My name is AL SWEIGART and I am 4,000 years old'
for word in string.split():
    print(len(word))

