def noOfVowels(word):
    fre=0
    word=word.lower()
    for i in word:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            fre+=1

    return fre

sen=input('Enter the Sentence\n')
wordList=sen.split(' ')
for i in range(0,len(wordList)-1):
    for j in range(0,len(wordList)-1-i):
        if noOfVowels(wordList[j])>noOfVowels(wordList[j+1]):
            tmp=wordList[j]
            wordList[j]=wordList[j+1]
            wordList[j+1]=tmp
            print(wordList)
for i in wordList:
    print(i,end=' ')



import re

