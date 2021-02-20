'''
Given a String, the task is to write a Python program to convert its characters to uppercase randomly.

Examples:

Input : test_str = 'geeksforgeeks'
Output : GeeksfORgeeks

Explanation : Random elements are converted to Upper case characters.

Input : test_str = 'gfg'
Output : GFg

Explanation : Random elements are converted to Upper case characters.
'''
import random as r
def execute():
    #test_str = input('Enter the String\n')
    test_str='geeksforgeeks'
    ls = list(test_str)
    randomNumOfRun = r.randint(0, len(ls))
    print('No of loops = ',randomNumOfRun)
    for i in range(0, randomNumOfRun):
        choiceOfIndex = list(range(len(ls)))
        choiceByRandom = r.choice(choiceOfIndex)
        print('Choice by random = ',choiceByRandom)
        ls[choiceByRandom] = ls[choiceByRandom].upper()

    for i in ls:
        print(i, end='')
    print('\n')
    if ls==list('GeeksfORgeeks'):
        print('YYYYYYYYEEEEEEEEEEEESSSSSSSSSSSSSSSSSSS')

for i in range(1000):
    execute()

