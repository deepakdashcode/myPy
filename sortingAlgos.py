def bubbleSort(ls):
    for i in range(0,len(ls)-1):
        for j in range(0,len(ls)-i-1):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls

def selectionSort(ls):
    for i in range(0,len(ls)-1):
        maxValue=ls[i]
        maxIndex=i
        for j in range(i+1,len(ls)):
            if ls[j]>maxValue:
                maxValue=ls[j]
                maxIndex=j
        ls[i],ls[maxIndex]=ls[maxIndex],ls[i]
    return ls

ls=[1,2,2443,546,54,6657,]#descending
ls1=[1432,543,74,2341,563,4]#Ascending
ls1=bubbleSort(ls1)
ls=selectionSort(ls)
print(ls)
print(ls1)
