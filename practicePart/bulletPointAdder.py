# ! python3
# bulletPointAdder.py - Adds wikipidia bullet points to the start
# of each line of text on the clipboard

import pyperclip as py
text = py.paste()
list = text.split('\n')
for i in range(len(list)):
    list[i] = '* ' + list[i]
text = '\n'.join(list)
py.copy(text)

print(text) 