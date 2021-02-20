'''
A valid password is the one which has min len =6 and starts with a number
'''
password=input('Enter the password\n')
if password[0].isnumeric() and len(password)>=6:
    print('Password Accepted')
else:
    print('Invalid password')