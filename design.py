'''
     0   1   2   3   4
0    *   *   *

1    *           *

2    *               *

3    *           *

4    *   *   *

'''
def printPattern(n):
    for i in range(0,n):
        for j in range(0,n):
            if j==0:
                print("*",end=' ')

            elif j<(int(n/2)) and (i==0 or i==n-1):
                print("*",end=' ')

            elif i <(int(n/2)) and (j-i)==int((n-1)/2):
                print("*",end=' ')
            elif i >((n/2)+1) and (i+j)==n+1:
                print("*",end=' ')
            else:
                print(" ",end="")

        print()




n=int(input('Enter the value of n \n'))

printPattern(n)
