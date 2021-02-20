'''
Consider piglatin of a word as remove first character append it to last and add ay
find piglatin if a sentence
'''
def piglatin(word):
    word=word[1:]+word[0]+'ay'
    return word
    pass

sen=input('Enter the Sentence\n')
words=sen.split()
for i in range(0,len(words)):
    words[i]=piglatin(words[i])
for i in words:
    print(i,end=' ')
