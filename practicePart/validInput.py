while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    else:
        print('Please enter a valid age')

while True:
    print('Enter your PASSWORD:')
    password = input()
    if password.isalnum():
        break
    else:
        print('Please enter a valid password, containing only letters and numbers')
