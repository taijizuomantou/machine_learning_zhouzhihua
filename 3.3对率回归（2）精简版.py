import numpy as np
import csv
d = 2
m = 17
f = csv.reader(open("watermelon3_0_Ch.csv","r"))
x = np.random.rand(m,d)
y = np.random.randn(m,1)
for i,line in enumerate(f):
    if i == 0:
        continue
    x[i - 1][0] = line[7]
    x[i - 1][1] = line[8]
    if line[9] == "是":
        temp = 1
    else:
        temp = 0
    y[i - 1] = temp
B =  np.random.rand(d + 1,1) 
X = np.concatenate((x,np.ones((m,1))),axis = 1)
tx = X
X = X.T
a = 0.1
for i in range(2000):
    mul = np.dot(X.T,B)
    dB = np.zeros((1,3))
    p = np.exp(mul) / (1 + np.exp(mul))
    d1 = np.sum(tx * (y - p),0)
    d2 = np.dot(tx.T,p * (1 - p) * tx) 
    dB = dB + np.dot(np.linalg.inv(d2),d1)
    B = B + a * dB.T
print(B)
yy = np.dot(B.T,X)
ans = np.exp(yy) / (1 + np.exp(yy))
ypred = np.where(ans > 0.5,"是","否")
print(ypred)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
tx = x.T
ax.scatter(tx[0].T,tx[1].T, y.T,c = 'r')
px1 = np.linspace(0.0, 1.0, num=50).reshape(50,1)
px2 = np.linspace(0.0, 1.0, num=50).reshape(50,1)
px = np.concatenate((px1,px2,np.ones((50,1))),axis = 1)
z = 1/(1 + np.exp(-np.dot(B.T,px.T).T))
px1,px2=np.meshgrid(px1,px2)#必须有
ax.plot_surface(px1, px2,z,rstride=1, cstride=1, cmap=plt.cm.coolwarm)
plt.show()

