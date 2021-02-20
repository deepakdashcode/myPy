'''
Reverse the characters in all words in a line including numbers, but leave special characters and symbols untouched in the same position. Consider the below examples.

Input: ‘Bangalore is@#$!123 locked again in jul2020’ should change to
Output: ‘erolagnaB si@#$!321 dekcol niaga ni 0202luj’

Input: ‘Bangalore is@#$!123locked locked again in jul2020’ should change to
Output: ‘erolagnaB si@#$!dekcol321 dekcol niaga ni 0202luj’
'''

def reverse(word):
    s=''
    for i in word:
        s=i+s
    return s

def containsSpecial(word):
    for i in word:
        if i.isalnum()==False and i.isspace()==False:
            return True
    return False

def isSpecial(character):
    if character.isalnum() == False and character.isspace() == False:
        return True
    else:
        return False

def manipulateSpecial(word):
    word+='@'
    charList=[]
    s=''
    i=0
    while(i<len(word)):

        if isSpecial(word[i])==False:
            s=word[i]+s
        else:
            #si@#$!321
            charList.append(s)
            s=''
            for j in range(i,len(word)):
                if isSpecial(word[j]):
                    s=s+word[j]
                else:
                    i=j-1
                    break

            charList.append(s)
            s=''
        i+=1
    requiredString=''
    for i in range(0,len(charList)-1):
        requiredString+=charList[i]
    return requiredString






test_str=input('Enter the String\n')
test_str.strip()
wordList=test_str.split(' ')
newWordList=[]
for i in wordList:
    if containsSpecial(i)==False:
        newWordList.append(reverse(i))
    else:
        newWordList.append(manipulateSpecial(i))

s=''
for i in newWordList:
    s+=i+' '
print(s)

