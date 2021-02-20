def pattern1(num):
    '''
    Pattern:1
    Input=6

    5 4 3 2 1 1 2 3 4 5

    5 4 3 2 2 3 4 5

    5 4 3 3 4 5

    5 4 4 5

    5 5
    '''
    for i in range(1,num):
        for j in range(num-1,i-1,-1):
            print(j,end=' ')
        for k in range(i,num):
            print(k,end=' ')
        print()

def pattern2(num):
    '''
    Pattern:
    10

    10 8

    10 8 6

    10 8 6 4

    10 8 6 4 2
    Code:
    rows = 5
    '''
    for i in range(num*2,2-1,-2):
        for j in range(num*2,i-1,-2):
            print(j,end=' ')
        print()

def pattern3(num):
    '''
    Pattern:
    Input=7
    0

    0 1

    0 2 4

    0 3 6 9

    0 4 8 12 16

    0 5 10 15 20 25

    0 6 12 18 24 30 36
    '''
    table=0
    for i in range(0,num):
        for j in range(0,i+1):
            print(table*j,end=' ')
        table+=1
        print()

def pattern4(num):
    '''
    Pattern:
    Input=5
    1

    3 3

    5 5 5

    7 7 7 7

    9 9 9 9 9
    '''
    for i in range(1,num*2,2):
        for j in range(1,i+1,2):
            print(i,end=' ')
        print()





