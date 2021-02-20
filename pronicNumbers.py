'''


Python program to print all pronic numbers between 1 and 100
The pronic number is a product of two consecutive integers of the form: n(n+1).

For example:

6 = 2(2+1)= n(n+1),
72 =8(8+1) = n(n+1)
'''
def isPronic(num):
    import math
    #num = int(input('Enter the number\n'))
    n = int(math.sqrt(num))
    if n * (n + 1) == num:
        return True
        #print('Yes')
    return False

for i in range(1,1001):
    if isPronic(i):
        print(i)
