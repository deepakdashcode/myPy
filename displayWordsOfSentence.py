sen=input('Enter a sentence\n')
sen=sen+" "
words=sen.split(" ")
for i in words:
    if len(i)<1:
        pass
    elif i[0]=='C' or i[0]=='c' or i[0]=='D' or i[0]=='d':
        print(i)
