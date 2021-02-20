print('Enter the coordinates of the points')
x1, y1, x2, y2, x3, y3 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
k=(x1*x3*x3)-(x1*x2*x2)+(x1*y3*y3)-(x1*y2*y2)+(x3*x2*x2)-(x2*x3*x3)+(x1*x1*x2)-(x1*x1*x2)-(x1*x1*x3)+(y2*y2*x3)-(y3*y3*x2)+(y1*y1*x2)-(y1*y1*x3)
t=(x3*(y1-y2))+(x1*(y1-y3))-(x1*(y1-y2))-(x2*(y1-y3))
f=k/(2*t)
g=(((x2*x2) - (x1*x1) + (y2*y2) - (y1*y1) )/(2*(x1-x2)))-((k*(y1-y2))/(2*t*(x1-x2)))
c=-((x1*x1)+(y1*y1)+(2*g*x1)+(2*f*y1))
print("x^2 + y^2+ {}x + {}y + {}".format(2*g,2*f,c))

