'''
Given a String, ensure it has equal character frequencies, if not, equate by adding required characters.

Input : test_str = ‘geeksforgeeks’
Output : geeksforgeeksggkkssfffooorrr
Explanation : Maximum characters are 4 of ‘e’. Other character are appended of frequency 4 – (count of chars).

Input : test_str = ‘geksforgeeks’
Output : geeksforgeeksggksffoorr
Explanation : Maximum characters are 3 of ‘e’. Other character are appended of frequency 3 – (count of chars).
'''
def removeDuplicateCharacters(word):
    s=''
    for i in word:
        if i not in s:
            s=s+i
    return s
def fre(ch,word):
    count=0
    for i in word:
        if ch==i:
            count+=1
    return count


test_str=input('Enter the String\n')
subString=removeDuplicateCharacters(test_str)
frequencies=[]
for i in subString:
    f=fre(i,test_str)
    frequencies.append(f)

maxFre=max(frequencies)
for i in range(0,len(subString)):
    diffInFrequency=maxFre-frequencies[i]
    for j in range(0,diffInFrequency):
        test_str+=subString[i]

print(test_str)


