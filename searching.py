def linearSearch(ls,element):
    #If pos exists return pos else return -1
    pos=-2
    for i in range(0,len(ls)):
        if ls[i]==element:
            pos=i
            break
    return pos+1

# ls=[1,32,45,657,78,34,23,1,23]
# print(linearSearch(ls,45))

def binarySearch(ls,element):
    """

    :type ls: list
    :type element: int
    """
    #This works only for sorted lists
    ls.sort()
    minInd=0
    maxInd=len(ls)-1
    pos=-2
    while(minInd<maxInd):
        mid = int((minInd+maxInd) / 2)
        if(element==ls[mid]):
            pos=mid
            break
        elif element>ls[mid]:
            minInd = mid+1
        elif element<ls[mid]:
            maxInd = mid-1
        print(mid)

    return pos+1

ls=[1,32,45,657,78,34,23,1,23]
ls.sort()
print(ls)
print(binarySearch(ls,45))
# [1, 1, 23, 23, 32, 34, 45, 78, 657]



