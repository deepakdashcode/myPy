x,y=0,0
increment=10
n=int(input('Enter the number\n'))
evenCount=0
oddCount=0
noOfIterations=0
# for i in range(1,n+1):
#     if i%4==0:
#         y=y-increment
#     elif i
testvalue=0
for i in range(1,n+1):
    noOfIterations+=1

    if noOfIterations%2==0:
        evenCount+=1
        if evenCount%2==0:
            y=y-increment
        else:
            y=y+increment
    else:
        oddCount+=1
        if oddCount%2==0:
            x=x-increment
        else:
            x=x+increment
    increment+=10
    if noOfIterations%5==0:
        noOfIterations=0
        oddCount,evenCount=evenCount,oddCount
    print('Step {}'.format(i))
    print('x , y = ({},{})'.format(x, y))



print('x , y = ({},{})'.format(x,y))

