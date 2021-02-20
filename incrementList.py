'''

Given the Strings list, write a Python program to increment strings that are numeric by K.

Examples:

Input : test_list = [“gfg”, “234”, “is”, “98”, “123”, “best”, “4”], K = 6
Output : [‘gfg’, ‘240’, ‘is’, ‘104’, ‘129’, ‘best’, ’10’]
Explanation : 234, 98 and 4 are incremented by 6 in result.

Input : test_list = [“gfg”, “234”, “is”, “98”, “123”, “best”, “4”], K = 4
Output : [‘gfg’, ‘238’, ‘is’, ‘102’, ‘129’, ‘best’, ‘8’]
Explanation : 234, 98 and 4 are incremented by 4 in result.
'''

ls=eval(input("Enter the list\n"))
k=int(input('Enter the value of k\n'))
for i in range(0,len(ls)):
    if ls[i].isdigit():
        ls[i]=str(int(ls[i])+k)
print(ls)