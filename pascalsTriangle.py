# def getNextElement(element):
#     s = '0' + element
#     s1 = element + '0'
#     n=''
#     for i in range(0, len(s)):
#         num = int(s[i])+int(s1[i])
#         n=n+str(num)+' '
#
#     return n.strip()
def getNextElement(element):
    el = element.copy()
    for i in range(0, len(el)):
        el[i] = int(el[i])
    s1=[0]
    s1=s1+el
    s2=[]
    s2=el.copy()
    s2.append(0)
    s3=[]
    for i in range(0,len(s1)):
        s3.append(s1[i]+s2[i])

    return s3


    #print(el)

l=[1]
n=int(input('Enter the number of lines\n'))
for i in range(0,n):
    for j in range(0,n-i+1):
        print(" ",end='')
    print(l)
    l=getNextElement(l)



#print(getNextElement('15101051'))

# element='1 5 10 10 5 1'
# el=element.split(' ')
# for i in range(0,len(el)):
#     el[i]=int(el[i])
# print(el)