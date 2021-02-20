word=input('Enter the String\n')
word1=input('Enter the String\n')
if word.find(word1)==0:
    print(word1,'is a prefix of ',word)
elif word1.find(word)==0:
    print(word,'is a prefix of ',word1)
else:
    print('neither is a prefix of other')