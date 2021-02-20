
def fre(ch, s):
    f = 0
    for i in s:
        if ch == i:
            f = f + 1
    return f
noOfCorrect=0
f1=open('correctAnswers.txt')
f2=open('answered.txt')
correctText=f1.read()
answeredText=f2.read()
correctList=correctText.split("\t")
answeredList=answeredText.split("\t")

for i in range(0,len(correctList)):
    if(correctList[i]!='' and answeredList[i]!=''):
        if(int(correctList[i])==int(answeredList[i])):
            noOfCorrect+=1
totalNoOfQuestions=fre("\t",correctText)
print("Total Number of Questions = ", totalNoOfQuestions)
print("Total Number of correct Questions = ", noOfCorrect)
per=(noOfCorrect/totalNoOfQuestions)*100
print("Percentage = ",per)
