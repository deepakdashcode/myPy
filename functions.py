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

print(fre('',''))
print(max([0.0,0,0000,1212]))