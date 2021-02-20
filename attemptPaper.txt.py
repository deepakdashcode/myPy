def removeBraces(a):
    w=''
    for i in a:
        if i!='[' and i!=']':
            w=w+i
    return w

def removeQuotes(a):
    w=''
    for i in a:
        if i!="'":
            w=w+i
    return w


f = open('questions.txt')
f1 = open('options.txt')
f2= open('answered.txt','w')
text = f.read()
options = f1.read()
options=removeBraces(options)
newLs=[]
newLs=options.split("\t")
optList=[]
for i in newLs:
    opt1List = removeQuotes(i).split(',')
    optList.append(opt1List)


qNo=0

# opt1List=removeQuotes(newLs[0]).split(',')
# print(optList)

# print(newLs[0])
# print(newLs)
w = ''

optNumber = 0
for i in text:
    num = 0
    if i != '\t':
        print(i, end='')
    else:
        print()
        for j in optList[qNo]:
            print("({})".format(num+1), j)
            num+=1
        optNumber = int(input('Enter the option number\n'))
        optNumber = optNumber - 1
        f2.write(str(optNumber) + "\t")
        qNo += 1




