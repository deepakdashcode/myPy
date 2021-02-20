def isPalindrome(word):
    ls1 = list(word)
    ls2 = ls1.copy()
    ls2.reverse()
    if ls2 == ls1:
        return True
    else:
        return False


word = input('Enter the string\n')

palindromeList = []
for i in range(0, len(word)):
    for j in range(i, len(word)):
        testWord = (word[i:j + 1])
        if isPalindrome(testWord) and len(testWord) > 1:
            # print(testWord)
            palindromeList.append(testWord)

longestWord = palindromeList[0]
for i in palindromeList:
    if len(i) > len(longestWord):
        longestWord = i

print(longestWord)
