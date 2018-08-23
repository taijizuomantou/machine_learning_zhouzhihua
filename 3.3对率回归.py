#特别注意。当返回数组的shape是（3，）时候，再与（3,1）做运算结果就会变成（3,3）。
#可以简单的改成与（1,3）做运算，结果正常
#注意绘3d面一定要有px1,px2=np.meshgrid(px1,px2) 只要在将x,y,z写在一起之前有就行
# =============================================================================
# import numpy as np
# import csv
# f = csv.reader(open("watermelon3_0_Ch.csv","r"))
# x = [[] for i in range(17)]
# print(x)
# y = []
# for i,line in enumerate(f):
#     if(i == 0):
#         continue
#     print(line[7])
#     x[i - 1].append(line[7])
#     x[i - 1].append(line[8])
#     print(x)
# =============================================================================
import numpy as np
import csv
d = 2#属性个数
m = 17#样例个数
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
#B (3,1) X(3,M) *(1,M)
# =============================================================================
# 循环牛顿法
# for i in range(2000):
#     mul = np.dot(B.T,X)
#     dB = np.zeros((1,3))
#     d1 = np.zeros((1,3))
#     d2 = np.zeros((3,3))
#     for j in range(m):
#         temp = mul[0][j]
#         p = np.exp(temp) / (1 + np.exp(temp))
#         xtemp = tx[j].reshape((-1,1))
#         d1 = d1 + tx[j] * (y[j] - p)
#         d2 = d2 + np.dot(xtemp,xtemp.T) * p * (1 - p)
# 
#     dB = np.dot(d1,np.linalg.inv(d2) )
#     
#     B = B + a * dB.T
# print(B)
# =============================================================================
# =============================================================================
# 数组梯度下降法
# for i in range(2000):
#     mul = np.dot(X.T,B)
#     dB = np.zeros((1,3))
#     p = np.exp(mul) / (1 + np.exp(mul))
#     d1 = np.sum(tx * (y - p),0)
#     dB = dB +d1
#     B = B + a * dB.T
# print(B)
# =============================================================================

#数组牛顿法
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

# =============================================================================
# 绘图
# =============================================================================
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#三维图
fig = plt.figure()
ax = Axes3D(fig)
#绘制散点图
temp0 = np.where(y == 0)
temp1 = np.where(y == 1)

ax0 = x[temp0[0],:]
ax1 = x[temp1[0],:]

ax.scatter(ax0[:,0],ax0[:,1] ,y[temp0].T,c = 'r')
ax.scatter(ax1[:,0],ax1[:,1], y[temp1].T,c = 'g',marker = 'x')
#绘制曲面
px1 = np.linspace(0.0, 1.0, num=50).reshape(50,1)
px2 = np.linspace(0.0, 1.0, num=50).reshape(50,1)
px = np.concatenate((px1,px2,np.ones((50,1))),axis = 1)
z = 1/(1 + np.exp(-np.dot(B.T,px.T).T))
px1,px2=np.meshgrid(px1,px2)#必须有
ax.plot_surface(px1, px2,z,rstride=1, cstride=1, cmap=plt.cm.coolwarm)

plt.show()

#其实就是绘制b0 * x1 + b1 * x2 + b2 = 0的那条线
#当x1 = 0时，x2 = -b2/b1
#当x1 = 0.9时 x2 = (- b2 - 0.9 * b0) / b1
plt.scatter(ax0[:,0],ax0[:,1] ,c = 'r')
plt.scatter(ax1[:,0],ax1[:,1], c = 'g',marker = 'x')
plt.plot([0,0.9],[-B[2]/B[1],(-B[2]-0.9*B[0])/B[1]])
plt.show()