'''
Given a String of date of format YYYYMMDD, our task is to compute the life path number.  Life Path Number is the number obtained by summation of individual digits of each element repeatedly till single digit, of datestring. Used in Numerology Predictions.

Examples:

Input : test_str = “19970314”

Output : 7

Explanation : 1 + 9 + 9 + 7 = 26 , 2 + 6 = 8 [ year ] ; 0 + 3 = 3 [ month ] ;
 1 + 4 = 5 [ day ]. 5 + 3 + 8 = 16 ; 1 + 6 = 7.
'''
def sumOfDigits(num):
    sum=0
    while(num>0):
        d=num%10
        sum=sum+d
        num//=10
    return sum

def lifePath(string):
    year=int(string[0:4])
    month=int(string[4:6])
    day=int(string[-2:])
    sumOfAll=0
    #print(year,month,day)
    #singleYear=singleMonth=singleDay=0
    print('loop in')
    while(year>10):
        year=sumOfDigits(year)
        print('Year is ',year)
    print('loop 1 out')
    while (month > 10):
        month = sumOfDigits(month)
        print('month is ',month)
    print('loop 2 out')
    print(day)
    while (day > 10):
        day = sumOfDigits(day)
        print('Day is ',day)
    print('loop 3 out')
    sumOfAll=year+month+day

    while (sumOfAll > 10):
        sumOfAll = sumOfDigits(sumOfAll)
        print('sum is ',sumOfAll)

    return sumOfAll


test_str=input('Enter the String in the format YYYYMMDD\n')
print(lifePath(test_str))


