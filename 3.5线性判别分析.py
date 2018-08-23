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

plt.scatter(y0x1,y0x2)
plt.scatter(y1x1,y1x2,marker = 'x',c = 'r' )
px1 = np.linspace(0.0, 1.0, num=50).reshape(50,1)
px2 = np.linspace(0.0, 1.0, num=50).reshape(50,1)
px = np.concatenate((px1,px2),axis = 1)
y = np.dot(px,w)
plt.plot(px,y)
plt.show()


# =============================================================================
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# tx = x.T
# ax.scatter(tx[0].T,tx[1].T, y.T,c = 'r')
# px1 = np.linspace(0.0, 1.0, num=50).reshape(50,1)
# px2 = np.linspace(0.0, 1.0, num=50).reshape(50,1)
# px = np.concatenate((px1,px2),axis = 1)
# print(np.shape(px))
# z = np.dot(px,w.T).reshape(-1,1)
# print(np.shape(z))
# px1,px2=np.meshgrid(px1,px2)#必须有
# ax.plot_surface(px1, px2,z,rstride=1, cstride=1, cmap=plt.cm.coolwarm)
# plt.show()
# 
# 
# =============================================================================
