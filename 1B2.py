import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import *
x = linspace(0, 4 ,70)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $sin(x)$')

y = sin(x)
y1 = x
y2 = x - x*x*x/(3*2*1)
y3 = x - x*x*x/(3*2*1) + x*x*x*x*x/(5*4*3*2*1)
y4 = x - x*x*x/(3*2*1) + x*x*x*x*x/(5*4*3*2*1) - x*x*x*x*x*x*x/(7*6*5*4*3*2*1)

plt.plot(x, y, color = "#FF0000")
plt.plot(x, y1, color = "#00FF00")
plt.plot(x, y2, color = "#0000FF")
plt.plot(x, y3, color = "#FF00FF")
plt.plot(x, y4, color = "#FFFF00")

plt.show()
