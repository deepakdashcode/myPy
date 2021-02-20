import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-100,100,1000)

def f(x):
    return x**2

def fun(x,a):
    return x**2/(4*a)


#plt.plot(x,f(x))
plt.plot(x,fun(x,1))


plt.show()
