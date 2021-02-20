'''
For ex - 2700
         =3^3*2^2*5^2

'''
def isPrime(num):
    noOfDiv = 0
    for i in range(1,num+1):
        if num % i==0:
            noOfDiv+=1
    if noOfDiv==2:
        return True
    else:
        return False


num=int(input('Enter the number\n'))
primeNumbersLessThanOrEqualToNumber=[]
for i in range(2,num+1):
    if isPrime(i):
        primeNumbersLessThanOrEqualToNumber.append(i)
tempNum=num

noOfTimesPrimeNumPresent=[]
for i in primeNumbersLessThanOrEqualToNumber:
    noOfTimes=0
    while(True):
        if tempNum%i==0:
            tempNum=tempNum/i
            noOfTimes+=1
        else:
            break
    noOfTimesPrimeNumPresent.append(noOfTimes)

s=''
for i in range(0,len(primeNumbersLessThanOrEqualToNumber)):
    if noOfTimesPrimeNumPresent[i]!=0:
        s+=(str(primeNumbersLessThanOrEqualToNumber[i])+' ^ '+str(noOfTimesPrimeNumPresent[i])+" * ")
print(s.strip('* '))

