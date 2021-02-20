'''
Given the String list, write a Python program to count pairs of reverse strings.

Examples:

Input : test_list = [“geeks”, “best”, “tseb”, “for”, “skeeg”]
Output : 2
Explanation : geeks, skeeg and best, tseb are 2 pairs of reverse strings available.

Input : test_list = [“geeks”, “best”, “for”, “skeeg”]
Output : 1
Explanation : geeks, skeeg is 1 pair of reverse strings available.
'''
def reverse(word):
    s=''
    for i in word:
        s=i+s
    return s

#print(reverse('geeks'))

ls=[]
for i in range(0,int(input('Enter the number of words\n'))):
    if i==0:
        print('Enter the words')
    ls.append(input())

count=0
for i in ls:
    if reverse(i) in ls:
        count+=1

count=int(count/2)
print(count)

