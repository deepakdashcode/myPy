tup=eval(input())
ls=list(tup)
#ls.sort(key=len)
length=ls[0]
for i in range(0,len(ls)-1):
    for j in range(0,len(ls)-i-1):
        if len(ls[j])>len(ls[j+1]):
            ls[j+1],ls[j]=ls[j],ls[j+1]

tup=tuple(ls)
print(tup)