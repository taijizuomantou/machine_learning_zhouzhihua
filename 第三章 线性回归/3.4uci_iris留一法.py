#uci iris 多分类任务 模型训练
#留一法错了8个
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
aX = np.concatenate((x,np.ones((m,1))),axis = 1)
a = 0.001
def f(x):
    print(np.shape(x))
error = 0

for k in range(m):
    yy = np.zeros((num,1))
    for i in range(1,4):#1,2 ,1,3 2,3
        dx = np.delete(aX,k,axis = 0)
       # print(dx)
        dy = np.delete(y,k,axis = 0)
        dnum = np.where(dy != i)
       # print(dnum)
        ttx = dx[dnum[0],:]
        ty = dy[dnum[0],:]
        #y1 表示当类别为1,2时 y1 = 1，当类别为2,3时y1 = 2,当类别为3,1时y1 = 3
        if i + 1 > 3:y1 = i + 1 - 3
        else: y1 = i + 1
        ty = np.where(ty == y1,1,0)
        mm = len(ty)
        #print(mm)
        tx = ttx
        X = ttx.T
        B =  np.random.rand(d + 1,1)  * 0.01
        #print(ty)
        #print(ty)
        for j in range(5000):
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
        ans = np.dot(aX[k,:],B)
        #print(aX[k])
        #print(ans)
        ans = np.exp(ans) / (1 + np.exp(ans))
        #print(ans)
        if(ans > 0.5):
            if(i + 1 > 3):yy[i - 1] = i + 1 - 3
            else:yy[i - 1] = i + 1
        else:
            if(i + 2 > 3):yy[i - 1] = i + 2 - 3
            else:yy[i - 1] = i + 2  
        #print(yy[i - 1])
    yy = yy.flatten()
    yy = yy.astype(int)
    #print(yy)
    count = np.bincount(yy)
    ypred = np.argmax(count)
    #print(y[k,:])
    #print(ypred)
    #print(yy)
    if(ypred != y[k,:]):
        error = error + 1
print(error)
    
    #print(aB)
# =============================================================================
#     yy = np.dot(X.T,B)
#     ans = np.exp(yy) / (1 + np.exp(yy))
#     ypred = np.where(ans > 0.5,1,0)
#     print(ypred)
#     print(np.sum(ypred))
# =============================================================================

