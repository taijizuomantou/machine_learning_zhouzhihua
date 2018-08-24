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

temp0 = np.where(y == 0)
temp1 = np.where(y == 1)

ax0 = x[temp0[0],:]
ax1 = x[temp1[0],:]

u0 = np.mean(ax0,axis = 0)
u1 = np.mean(ax1,axis = 0)

sw = np.dot((ax0 - u0).T,ax0 - u0) + np.dot((ax1 - u1).T,ax1 - u1)

w = np.dot(np.linalg.inv(sw) , (u0 - u1).T)
#w = np.linalg.inv(sw) * (u0 - u1)
print(w)
y = np.dot(x,w.T)
#print(y)
import matplotlib.pyplot as plt
plt.scatter(ax0[:,0],ax0[:,1])
plt.scatter(ax1[:,0],ax1[:,1],marker = 'x',c = 'r' )
#直线不需要生成很多点
#其实就是绘制 w0 * x1 + w1 * x2 = 0的那一条线
#当x1 = 0时，x2 = 0
#当x1 = 0.9 时 x2 = -w0 * 0.9 / w1
ey = -0.9 * w[0] / w[1]

plt.plot([0,0.9],[0,ey])
plt.show()


