'''
Given a Strings list and substring, the task is to write a Python program to extract all the strings that has all the characters that can be used to make substring.

Examples:

Input : test_list = [“gfg”, “/”, “geeksforgeeks”, “best”, “for”, “geeks”], substr = “kgs”

Output : [“geeksforgeeks”, “geeks”]

Explanation : All kgs characters are present in both strings.



'''

def fre(ch,word):
    count=0
    for i in word:
        if ch==i:
            count+=1
    return count

def removeDuplicate(word):
    s=''
    for i in word:
        if i not in s:
            s+=i
    return s

def canMake(mainStr,subStr):
    distinctSubstr=removeDuplicate(subStr)
    for i in distinctSubstr:
        if fre(i,subStr) >fre(i,mainStr):
            return False
    return True


# print(canMake(mainStr='geeksforgeeks',subStr='kgs'))
# ls=eval(input('Enter the list\n'))

ls=[]
for i in range(0,int(input('Enter the number of Elements\n'))):
    ls.append(input('Enter Element {}'.format(i+1)))
subStr=input('Enter the substring\n')

for i in ls:
    if canMake(i,subStr):
        print(i)

