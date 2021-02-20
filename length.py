# f=open('temporaryStorage.txt')
# note=f.read()
# print(note)
# print(len(note))
f=open('questions.txt')
text=f.read()
w=''
s=''
for i in text:
    if i!='\t':
        print(i,end='')
    else:
        print()

