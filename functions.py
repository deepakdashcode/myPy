def fre(ch,word):
    count =0
    for i in word:
        if i==ch:
            count+=1
    return count

def max(ls):
    maximum=ls[0]
    for i in range(1,len(ls)):
        if maximum<ls[i]:
            maximum=ls[i]
    return maximum

    
print(fre('l','lala'))
print(max([1,2,3,5,21,1,1,2]))

print(fre('',''))

