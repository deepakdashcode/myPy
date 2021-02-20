'''
Practice Question of Sumita Arora
'''
credentials = {'Abc': 1234, 'cda': 2332}
username = input('Enter the username\n')
if username in credentials.keys():
    print('Valid user please enter your password\n')
    password = input('Enter the password\n')
    if str(credentials[username])==password:
        print('Yes valid password\nYou are logged in')
    else:
        print('Invalid Password')
else:
    print('Invalid username')
