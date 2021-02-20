'''
Given a list of strings, the task is to write a Python program to extract all characters that are same at a specified index of each element of a list.

Input : test_list = [“geeks”, “weak”, “beak”, “peek”]
Output : [‘e’, ‘k’]
Explanation : e and k are at same at an index on all strings.

Input : test_list = [“geeks”, “weak”, “beak”, “peer”]
Output : [‘e’]
Explanation : e is at same at an index on all strings.
'''

test_list=[]
for i in range(0,int(input('Enter the Number Of Elements\n'))):
    if i==0:
        print('Enter the elements')
    test_list.append(input())

common_list=[]
shortest_word=test_list[0]
shortest_length=len(test_list[0])
for i in range(1,len(test_list)):
    if len(test_list[i])<shortest_length:
        shortest_length=len(test_list[i])
        shortest_word=test_list[i]
for i in range(0,len(shortest_word)):
    condition=True
    for j in test_list:
        if j[i]!=shortest_word[i]:
            condition=False
            break
    if condition:
        common_list.append(shortest_word[i])

print(common_list)