n = int(input('Enter the Number of Elements\n'))
ls = []
for i in range(0, n):
    ls.append(float(input('Num {} = '.format(i + 1))))

mode=ls[0]
maxCount=ls.count(ls[0])
sum=0
for i in range(1,len(ls)):
    sum+=ls[i]
    newCount=ls.count(ls[i])
    if newCount>maxCount:
        maxCount=newCount
        mode=ls[i]
mean=sum/len(ls)
median=0
l=int(len(ls)/2)
if len(ls)%2==0:
    #l=len(ls)/2
    median=(ls[l]+ls[l+1])/2
else:
    median=ls[l+1]

print('MEAN {} MODE {} MEDIAN {}'.format(mean,mode,median))

