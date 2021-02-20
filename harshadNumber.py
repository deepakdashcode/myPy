'''
If a number is divisible by its sum of digits then its harshad
for ex 153
sum=9
Yes Harshad

'''
def sumOfDigits(num):
    sum=0
    while num>0:
        d=num%10
        sum=sum+d
        num = num//10
    return sum
def isHarshad(num):
    if num%sumOfDigits(num)==0:
        return True
    return False

for i in range(11,1001):
    if isHarshad(i):
        print(i)

