'''
Given: [a,b,c,....]
Expected: [a,a+b,a+b+c,....]
'''


def Sum(ls, start, end):
    s = 0
    for i in range(start, end + 1):
        s = s + ls[i]
    return s


n = int(input('Enter the Number of Elements\n'))
ls = []
for i in range(0, n):
    ls.append(float(input('Num {} = '.format(i + 1))))
newList=[]
for i in range(0,len(ls)):
    newList.append(Sum(ls,0,i))
print(newList)
