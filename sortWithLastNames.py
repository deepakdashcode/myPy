def getLastWord(sen):
    ls = sen.split()
    return ls[-1]


#ls=eval(input('Enter the Expression\n'))
ls=[]
n=int(input('Enter the number of names\n'))
print('Enter the names now')
for i in range(0,n):
    ls.append(input())

for i in range(0,len(ls)-1):
    for j in range(0,len(ls)-i-1):
        if getLastWord(ls[j]) > getLastWord(ls[j+1]):
            tmp=ls[j]
            ls[j]=ls[j+1]
            ls[j+1]=tmp

print(ls)
