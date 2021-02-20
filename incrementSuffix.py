'''

Given a String, the task is to write a Python program to increment the number which is at end of the string.

Input : test_str = ‘geeks006’
Output : geeks7
Explanation : Suffix 006 incremented to 7.

Input : test_str = ‘geeks007’
Output : geeks8
Explanation : Suffix 007 incremented to 8.

'''

test_str=input('Enter the String\n')
test_str.strip()
indexOfFirstNumberFromLast=-1
for i in range(len(test_str)-1,-1,-1):
    if test_str[i].isalpha():
        indexOfFirstNumberFromLast=i
        break

word=test_str[:i+1]
num=test_str[i+1:]
num=int(num)+1
result=word+str(num)
print(result)