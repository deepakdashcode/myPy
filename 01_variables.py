class Student:
    def __init__(self, id, percentage):
        self.id = id
        self.percentage = percentage

    def __str__(self):
        string = 'The id of Student is {}'.format(self.id) + "\n"
        string = string + 'The percentage of the student is {}'.format(self.percentage)
        return string

    def __gt__(self, other):
        if self.percentage > other.percentage:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.percentage >= other.percentage:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.percentage < other.percentage:
            return True
        else:
            return False

    def __le__(self, other):
        if self.percentage < other.percentage:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.percentage == other.percentage:
            return True
        else:
            return False

    def max(self, object):
        if self > object:
            return self
        else:
            return object

    def min(self, object):
        if self < object:
            return self
        else:
            return object


# stu1 = Student('Rohan', 98.9)
# stu2 = Student('Amit', 99)
# stu3 = Student('Subham', 98)
# stu4 = Student('Srikant', 100)
# l = [stu1, stu2, stu3, stu4]
# l.sort()
# l.reverse()
# for i in l:
#     print(i)
# print('Student ID\tPercentage')
# for i in l:
#     print(i.id,'\t\t\t\t',i.percentage)
l1=[]
n=int(input('Enter the number of Students\n'))
print('Enter the names and marks of each student respectively')

for i in range(0,n):
    try:
        name=input('Enter the name of Student {}\n'.format(i+1))
        percentage=float(input('Enter the percentage of Student {}\n'.format(i+1)))
    except:
        percentage = float(input('Enter the percentage of Student {}\n'.format(i + 1)))
    l1.append(Student(name,percentage))
l1.sort()
l1.reverse()
perList=[]
for i in l1:
    perList.append(i.percentage)
rankList=[1]
rank=1
for i in range(0,len(perList)-1):
    if (perList[i]>perList[i+1]):
        rank=rank+1
    rankList.append(rank)

print('Name\tPercentage\tRank')
for i in range(0,len(l1)):
    print(l1[i].id,'\t\t',l1[i].percentage,'\t\t',rankList[i])






