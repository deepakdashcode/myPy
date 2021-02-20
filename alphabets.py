# for i in range(65,91):
#     print(chr(i),end=' ')

'''
a
cc
eee
gggg

n=4
'''
n=int(input('Enter the value of n\n'))
inc=(n-1)*2
ini=1
s=''
for i in range(97,97+inc+1,2):
    for j in range(97,i+1,2):
        print(chr(i),end='')
    print()




