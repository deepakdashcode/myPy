# l=[1,22,323,53,32,23,21,2,12,12,21]
# for i in range(1,len(l)):
#     anchor=l[i]
#     j=i-1
#     while j>=0 and anchor < l[j]:
#         l[j+1] = l[j]
#         j-=1
#     l[j+1]=anchor
#     pass
# print(l)
# ls=[1,22,323,53,32,23,21,2,12,12,21]
# for i in range(1,len(ls)):
#     anchor=ls[i]
#     j=i-1
#     while j>=0 and anchor<ls[j]:
#         ls[j+1]=ls[j]
#         j = j - 1
#
#     ls[j+1]=anchor
#
# print(ls)

#
# ls=[1,3,2.1,4]
# for i in range(1,len(ls)):
#     anchor=ls[i]
#     j=i-1
#     while j>=0 and anchor < ls[j]:
#         ls[j+1]=ls[j]
#         j-=1
#     ls[j+1]=anchor
#
# print(ls)
#


# ls=[21,2,3,34,3,2,1,1,23,4,4,0]
# for i in range(1,len(ls)):
#     anchor=ls[i]
#     j=i-1
#     print('anchor is ',anchor)
#     while j >=0 and  anchor < ls[j]:
#
#         print('inner loop')
#         ls[j+1]=ls[j]
#         print(ls)
#         j-=1
#     ls[j+1]=anchor
#     print('After inner loop does its work j is ',j)
#     print(ls)
#     print('Outer iteration no {}'.format(i))
# print(ls)


