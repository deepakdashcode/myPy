sen=input('Enter the Sentence\n')
n=int(input('Enter the Word Length\n'))
wordList=sen.split()
s=''
for i in wordList:
    if len(i)!=n:
        s=s+i+' '

print(s)
