def lin(start,end,noOfValues):
    noOfValues=noOfValues-2
    diff=(end-start)/(noOfValues+1)
    newList=[start]
    for i in range(1,noOfValues+1):
        newList.append(start+(i*diff))
    newList.append(end)
    return newList

print(lin(1,8,5))