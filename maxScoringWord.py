'''
Given a String, the task is to write a Python program to compute maximum scoring words i.e words made of characters with a maximum positional summation.

Examples:

Input : test_str = ‘geeks must use geeksforgeeks for cs knowledge’

Output : geeksforgeeks

Explanation : Sum of characters positional values for “geeksforgeeks” word is maximum, hence result.

Input : test_str = ‘geeks love geeksforgeeks’

Output : geeksforgeeks

Explanation : Sum of characters positional values for “geeksforgeeks” word is maximum, hence result.
'''

'''
A=65 -----> 1
a=97 -----> 1

'''

def sumOfPosition(word):
    word=word.upper()
    s=0
    for i in word:
        add=ord(i) - 64
        s=s+add
    return s


test_str=input()
ls=test_str.split(' ')
word=''
sum=0
for i in ls:
    if sumOfPosition(i) > sum:
        sum=sumOfPosition(i)
        word=i
print(word)


