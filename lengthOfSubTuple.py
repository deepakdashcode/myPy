tup=eval(input())
#Expected to print their lengths
#output
#(2,3,1,3)
ls=[]
for i in tup:
    ls.append(len(i))

newTup=tuple(ls)
print(newTup)