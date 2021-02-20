'''
Given a String, the following program converts the alphabetic character around any digit to its uppercase.

Input : test_str = ‘geeks4geeks is best1 f6or ge8eks’
Output : geekS4Geeks is besT1 F6Or gE8Ek
Explanation : S and G are uppercased as surrounded by 4.
Input : test_str = ‘geeks4geeks best1 f6or ge8eks’
Output : geekS4Geeks besT1 F6Or gE8Ek
Explanation : S and G are uppercased as surrounded by 4.
'''
#Accepting Value from user
test_str=input('Enter the String\n')
#Converting String to lists
ls=list(test_str)
for i in range(0,len(ls)):
    #When element at index =0 is an integer we have to make the element at index 1 uppercased
    if i==0:
        if ls[0].isdigit():
            ls[1]=ls[1].upper()
    # When element at index len - 1 (last index) is an integer we have to make the second last element uppercased
    elif i==(len(ls)-1):
        if ls[len(ls)-1].isdigit():
            ls[-2]=ls[-2].upper()
    # When element is at any other index we have to make both nearby elements uppercased
    else:
        if ls[i].isdigit():
            ls[i-1]=ls[i-1].upper()
            ls[i+1]=ls[i+1].upper()
#Printing The list without newline
for i in ls:
    print(i,end='')
print('\n')
# initializing string
test_str = 'geeks4geeks is best1 f6or ge8eks7'

# printing original string
print("The original string is : " + str(test_str))

res = ''
for idx in range(len(test_str) - 1):
    if test_str[idx + 1].isdigit() or test_str[idx - 1].isdigit():
        res += test_str[idx].upper()
    else:
        res += test_str[idx]

    # printing result
print("Transformed String : " + str(res))

