'''
Given two strings, the task here is to write a python program that can test if they are almost similar. Similarity of strings is being checked on the criteria of frequency difference of each character which should be greater than a threshold here represented by K.

Input : test_str1 = ‘aabcdaa’, test_str2 = “abbaccd”, K = 2

Output : True

Explanation : ‘a’ occurs 4 times in str1, and 2 times in str2, 4 – 2 = 2, in range, similarly, all chars in range, hence true.

Input : test_str1 = ‘aabcdaaa’, test_str2 = “abbaccda”, K = 3



Output : True

Explanation : ‘a’ occurs 5 times in str1, and 3 times in str2, 5 – 3 = 2, in range, similarly, all chars in range, hence true.
'''


def removeDuplicate(word):
    """

    :rtype: str
    """
    s = ''
    for i in word:
        if i not in s:
            s += i
    return s


def fre(ch, word):
    count = 0
    for i in word:
        if i == ch:
            count += 1
    return count


str1 = input('Enter the first String\n')
str2 = input('Enter the second String\n')
k=int(input('Enter the value of K\n'))
nonDuplicateStr1=removeDuplicate(str1)
nonDuplicateStr2=removeDuplicate(str2)

dict1=dict()
for i in nonDuplicateStr1:
    dict1[i]=fre(i,str1)


for i in nonDuplicateStr2:
    dict1[i]=fre(i,str1)


dict2=dict()
for i in nonDuplicateStr2:
    dict2[i]=fre(i,str2)

test=True

for i in nonDuplicateStr1:
    dict2[i]=fre(i,str2)


for i in dict1:
    if abs(dict1[i]-dict2[i]) > k:
        test=False
        break

print(dict1,dict2)
if test:
    print("YES Similar")
else:
    print("NOT similar")





