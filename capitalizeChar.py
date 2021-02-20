word=input('Enter the String\n')
character=input('Enter the Character\n')
if len(character)>1:
    print('Invalid Character')
else:
    newString=''
    for i in word:
        if i==character:
            newString=newString+i.upper()
        else:
            newString+=i.lower()
    print(newString)
