ls = []
n = int(input('Enter the number of elements\n'))
for i in range(0, n):
    ls.append(float(input()))

divByTwo = divByThree = divByNine = 0

for i in ls:
    if i % 2 == 0:
        divByTwo += 1

    if i % 3 == 0:
        divByThree += 1

    if i % 9 == 0:
        divByNine += 1

print('Div by 2 ', divByTwo)
print('Div by 3 ', divByThree)
print('Div by 9 ', divByNine)
