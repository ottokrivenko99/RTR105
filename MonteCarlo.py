# 1. N vienmērīgi sadalīti gadījuma skaitļi
# N uniformly distributed random numbers

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

import numpy
##print(numpy.random.__doc__)
##print(numpy.random.uniform.__doc__)

a = 0
b = 5
N = 10000

##(pseido) gadījuma skaitļu ģenerātora grauds
##numpy.random.seed(1)

#x= numpy.random.uniforma(a,b,N)
#numpy.random.normal(a,b,N)


x = numpy.random.uniform(a,b,N)
k = [0, 0, 0, 0, 0]
for i in range(N):
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] < 2:
        k[1] = k[1] + 1
    elif x[i] < 3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1

print(k)
print(sum(k))

y= numpy.random.uniform(a,b,N)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('funkcija $cos(x)$')
#plt.plot(x,y, 'ko')
N1 = 0
for i in range(N):
    if y[i] < x[i]:
        plt.plot(x[1], y[1], 'go')
        N1 = N1 +1
    else:
        plt.plot(x[1], y[1], 'ro')
plt.show()

S_zinaamais + (b-a) * (b-a)
S_nezinaamais = 1. * s_zinamais * N1/N
print(S_nezinaamais)
