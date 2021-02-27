'''
Input : test_str = ‘geeks must use geeksforgeeks for cs knowledge’

Output : geeksforgeeks

Explanation : Sum of characters positional values for “geeksforgeeks” word is maximum, hence result.


Input : test_str = ‘geeks love geeksforgeeks’

Output : geeksforgeeks

Explanation : Sum of characters positional values for “geeksforgeeks” word is maximum, hence result.
'''
def evaluateWord(word):
    word=word.lower()
    s=0
    for i in word:
        s=s+ord(i)-97
    return s

test_str=input('Enter the Sentence\n')
words=test_str.split()
scoresOfWords=[]
for i in words:
    scoresOfWords.append(evaluateWord(i))

largestWord=words[0]
highestScore=scoresOfWords[0]
for i in range(1,len(words)):
    if scoresOfWords[i]>highestScore:
        highestScore=scoresOfWords[i]
        largestWord=words[i]

print(largestWord)    
print(highestScore)



