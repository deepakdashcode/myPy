arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '.']


def fre(ch, s):
    f = 0
    for i in s:
        if ch == i:
            f = f + 1
    return f
# def removeCharFromString(ch,s):
#     a=''
#     for i in s:
#         if i!=ch:
#             a=a+i
#     return a
#
#
# def removeExcept(a,*args):
#
#     for i in args:
#         a=removeCharFromString(i,a)
#     return a




def isBinary(a):
    if fre('.', a) > 1:
        return False
    else:
        for i in a:
            if i != '1' and i != '0' and i != '.':
                return False
    return True


# def isHexadecimal(a):
#     if(fre('.',a)>1):
#         return False
#     else:

def decTonewBase(num,base):
    decimal=num-int(num)
    num=int(num)
    s=''
    while num!=0:
        d=num%base
        s=arr[d]+s
        num=int(num/base)
    s=s+'.'
    newNumber=-1
    copyOfDecimal=decimal
    decOfNewNum=-1

    while (newNumber!=0 and decOfNewNum !=copyOfDecimal):
        newNumber=decimal*base
        decOfNewNum=newNumber-int(newNumber)
        newNumber=int(newNumber)
        decimal=decOfNewNum
        s=s+arr[newNumber]
        if (decOfNewNum == 0 or decOfNewNum == copyOfDecimal):
            break
    return s


def decToHex(num):
    s=decTonewBase(num,16)
    if(s[0]=='.'):
        s='0'+s
    return s

def decToBinary(num):
    return float(decTonewBase(num,2))

def decToOctal(num):
    return float(decTonewBase(num,8))




def binToDec(a):
    if isBinary(a) == False:
        print('Some Error Occurred')
        pass
    if ('.' in a) == False:
        p = 0
        s = 0
        for i in range(len(a) - 1, -1, -1):
            num = int(a[i])
            s = s + (num * (2 ** p))
            p += 1
        return s
    else:
        beforePoint = a[:a.index('.')]
        afterPoint = a[a.index('.') + 1:]
        p = 0
        s = 0
        for i in range(len(beforePoint) - 1, -1, -1):
            num = int(a[i])
            s = s + (num * (2 ** p))
            p += 1

        p1 = -1
        for i in afterPoint:
            num = int(i)
            s = s + (num * (2 ** p1))
            p1 = p1 - 1
        return s

def hexToDec(a):

    if ('.' in a) == False:
        p = 0
        s = 0
        for i in range(len(a) - 1, -1, -1):
            num = int(arr.index(a[i]))

            s = s + (num * (16 ** p))
            p += 1
        return s
    else:
        beforePoint = a[:a.index('.')]
        afterPoint = a[a.index('.') + 1:]
        p = 0
        s = 0
        for i in range(len(beforePoint) - 1, -1, -1):
            num = int(arr.index(a[i]))
            s = s + (num * (16** p))
            p += 1

        p1 = -1
        for i in afterPoint:
            num = int(arr.index(i))
            s = s + (num * (16 ** p1))
            p1 = p1 - 1
        return s


# print(binToDec('110.11'))
# print(binToDec('1111111111111100000000000000011111111111111111111111110000000000000000000000000000000011111111111'))
# print(removeExcept('abcde','a','b'))
num=0.75
print(decToHex(num))
print(decToBinary(num))
print(decToOctal(num))
print(hexToDec('ffff'))
