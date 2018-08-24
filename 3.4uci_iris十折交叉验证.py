#uci iris 多分类任务 模型训练
import numpy as np
import csv
d = 4
m = 150
num = 3#d*(d - 1) / 2
f = csv.reader(open("uciiris.csv","r"))
x = np.random.rand(m,d)
y = np.random.randn(m,1)
temp = 0
for i,line in enumerate(f):
    for j in range(4):
        x[i][j] = line[j]
    if line[4] == "Iris-setosa":
        temp = 1
    elif line[4] == "Iris-versicolor":
        temp = 2
    else :
        temp = 3
    y[i] = temp
a = 0.001
def f(x):
    print(np.shape(x))
aB =  np.random.rand(d + 1,num) 
for i in range(1,num + 1):#1,2 ,1,3 2,3
    dnum = np.where(y != i)
    ttx = x[dnum[0],:]
    ty = y[dnum[0],:]
    #y1 表示当类别为1,2时 y1 = 1，当类别为2,3时y1 = 2,当类别为3,1时y1 = 3
    if i + 1 > 3:y1 = i + 1 - 3
    else: y1 = i + 1
    ty = np.where(ty == y1,1,0)
    mm = len(ty)
    #print(mm)
    X = np.concatenate((ttx,np.ones((mm,1))),axis = 1)
    tx = X
    X = X.T
    B =  np.random.rand(d + 1,1) 
   
    for j in range(2000):
         mul = np.dot(X.T,B)
         p = np.exp(mul) / (1 + np.exp(mul))
         d1 = np.dot(X,ty-p)
         d2 = np.dot(X,p * (1 - p) * X.T) 
         dB = np.dot(np.linalg.inv(d2),d1)
         B = B + a * dB
         #J = np.sum(-ty * mul + np.log(1 + np.exp(mul)))
         #print(J)
    #print(B)
    #print(B)
    aB[:,num - 1] = B.reshape(1,d + 1)

print(aB)
# =============================================================================
#     yy = np.dot(X.T,B)
#     ans = np.exp(yy) / (1 + np.exp(yy))
#     ypred = np.where(ans > 0.5,1,0)
#     print(ypred)
#     print(np.sum(ypred))
# =============================================================================

