'''
* * * * *
 * * * *
  * * *
   * *
    *
    when n=5
'''
n=int(input('Enter the value of n\n'))
for i in range(n,0,-1):
    for sp in range(0,n-i+1):
        print(" ",end="")
    for j in range(0,i):
        print("*",end=" ")
    print()
