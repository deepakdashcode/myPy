def binToDec(num):
    s=0
    k=0
    for i in range(len(num)-1,-1,-1):
        s=s+(2**k)*int(num[i])
        k+=1
    return s

    pass


user=''
group=''
publicUser=''
chmod=''

print('Enter Permissions for user')
user=user+(input('Enter the read permission for user 0 or 1\n'))
user=user+(input('Enter the write permission for user 0 or 1\n'))
user=user+(input('Enter the execute permission for user 0 or 1\n'))
chmod=chmod+str(binToDec(user))

print('Enter Permissions for group')
group=group+(input('Enter the read permission for group 0 or 1\n'))
group=group+(input('Enter the write permission for group 0 or 1\n'))
group=group+(input('Enter the execute permission for group 0 or 1\n'))
chmod=chmod+str(binToDec(group))

print('Enter Permissions for public')
publicUser=publicUser+(input('Enter the read permission for public 0 or 1\n'))
publicUser=publicUser+(input('Enter the write permission for public 0 or 1\n'))
publicUser=publicUser+(input('Enter the execute permission for public 0 or 1\n'))
chmod=chmod+str(binToDec(publicUser))

print(chmod)







