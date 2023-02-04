   
while spam <5 :
    print("hello form while loop")
    spam = spam + 1




nAme = ''
while True:
    print('please type your name :')
    nAme = input()
    if nAme == 'your name':
        break
print ('think you')



while True :
    print('Who are you ?')
    name = input()
    if name != 'Joe':
        continue    #returns to the while clause and starts the while code again if the condition is true
    print('Hello, Joe. What is the password? ')
    password = input()
    if password == 'swordfish':
        break   #jump out of the loop
print('Access granted.')



nm = 0
i = 0
while i <= 100:
    nm += i
    i += 1
print(nm)
