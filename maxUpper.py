'''
Giving a String, write a Python program to find maximum run of uppercase characters.

Examples:

Input : test_str = ‘GeEKSForGEEksISBESt’
Output : 5
Explanation : ISBES is best run of uppercase.

Input : test_str = ‘GeEKSForGEEKSISBESt’
Output : 10
Explanation : GEEKSISBES is best run of uppercase.
'''

test_str=input('Enter the String\n')
w=''
maxlen=0
for i in test_str:
    if i.isupper():
        w=w+i
    else:
        if len(w)>maxlen:
            maxlen=len(w)
        w=''

print(maxlen)