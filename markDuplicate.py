'''
Given a list, the task is to write a Python program to mark the duplicate occurrence of elements with progressive occurrence number.

Input : test_list = [‘gfg’, ‘is’, ‘best’, ‘gfg’, ‘best’, ‘for’, ‘all’, ‘gfg’]

Output : [‘gfg1’, ‘is’, ‘best1’, ‘gfg2’, ‘best2’, ‘for’, ‘all’, ‘gfg3’]

Explanation : gfg’s all occurrence are marked as it have multiple repetitions(3).


Input : test_list = [‘gfg’, ‘is’, ‘best’, ‘best’, ‘for’, ‘all’]

Output : [‘gfg’, ‘is’, ‘best1’, ‘best2’, ‘for’, ‘all’]

Explanation : best’s all occurrence are marked as it have multiple repetitions(2).
'''
def fre(word,list):
    count=0
    for i in list:
        if i.rstrip('0123456789')  == word:
            count+=1
    return count


test_list=[]
for i in range(0,int(input('Enter the value of n\n'))):
    if i==0:
        print('Enter the elements')
    test_list.append(input())
hashList=[]
for i in test_list:
    f=fre(i,hashList)
    f+=1
    if f>1:
        hashList.append(i+str(f))
    elif f==1 and fre(i,test_list)>1:
        hashList.append(i + str(f))

    else:
        hashList.append(i)

print(hashList)
