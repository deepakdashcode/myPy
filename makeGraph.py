from math import *
import numpy as np
import matplotlib.pyplot as plt
lowest=float(input('Enter the lowest limit\n'))
highest=float(input('Enter the highest limit\n'))
accuracy=int(input('Enter the accuracy\n'))
x=np.linspace(lowest,highest,accuracy)
fig, ax=plt.subplots()
ax.grid(True,which='both')
ax.axhline(y=0,color='k')
ax.axvline(x=0,color='k')
x=list(x)
expression=input('Enter the Expression\n')
expression=expression.replace('^','**')
def fun(x,exp=expression):
    y=eval(exp)
    return y
y=[]
for i in x:
    y.append(fun(i))
plt.plot(x,y)
# for i in range(0,len(x)):
#     print('X = {} , y={}'.format(x[i],y[i]))
plt.show()
