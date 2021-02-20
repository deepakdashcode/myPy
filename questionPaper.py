class Question:
    def __init__(self, Question ,options , correctAnswersPosition):
        self.Question=Question
        self.options=options
        self.correctAnswersPosition=correctAnswersPosition

    # def __init__(self,question , answer):
    #     self.question=question
    #     self.answer=answer
    def __str__(self):
        no=0
        string=self.Question
        string=string+"\n"
        for i in self.options:
            string=string+"({})".format(no+1)
            no+=1
            string=string+i+"\n"
        string=string+"Correct Answer is "+self.options[self.correctAnswersPosition]
        return string


print("Enter the total number of Questions")
quesList=[]
num=int(input())
for i in range(0,num):
    optNo = 0
    ques=input("Enter the question\n")
    optLis=[]
    print("Enter the options and press double enter to end options")
    while True:
        op=input('Enter Option Number {}\n'.format(optNo+1))
        optNo+=1
        if len(op)!=0:
            optLis.append(op)
        else:
            break
    print("Enter the position of the correct option")
    pos=int(input())
    question=Question(ques, optLis, pos-1)
    quesList.append(question)

f=open('questions.txt','w')
f1=open('options.txt','w')
f2=open('correctAnswers.txt','w')

for i in quesList:
    print(i)
    f.write(i.Question+"\t")
    f1.write(str(i.options)+"\t")
    f2.write(str(i.correctAnswersPosition)+"\t")





