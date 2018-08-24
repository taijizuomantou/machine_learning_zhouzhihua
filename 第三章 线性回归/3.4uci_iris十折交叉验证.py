#uci iris 多分类任务 模型训练
#留一法错了8个
#np.s_
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
K = 10
for k in range(K):#K = 10十折交叉验证
    yy = np.zeros((num,int(m/K)))
    dx = np.delete(aX,np.s_[k * 5:k * 5 + 5],axis = 0)
    dx = np.delete(dx,np.s_[k * 5 + 50:k * 5 + 55],axis = 0)
    dx = np.delete(dx,np.s_[k * 5 + 100:k * 5 + 105],axis = 0)
    dy = np.delete(y,np.s_[k * 5:k * 5 + 5],axis = 0)
    dy = np.delete(dy,np.s_[k * 5 + 50:k * 5 + 55],axis = 0)
    dy = np.delete(dy,np.s_[k * 5 + 100:k * 5 + 105],axis = 0)
    for i in range(1,num + 1):#1,2 ,1,3 2,3
        
       # print(dx)
        #print(np.shape(dy))
        dnum = np.where(dy != i)
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
        B =  np.random.rand(d + 1,1) * 0.01
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
        ax = np.concatenate((aX[k * 5:k * 5 + 5],aX[k * 5+50:k * 5 + 5 + 50],aX[k * 5 + 100:k * 5 + 5+ 100]), axis = 0)
        ans = np.dot(ax,B)
        ans = np.exp(ans) / (1 + np.exp(ans))
        tempp = np.where(ans > 0.5,i + 1,i + 2)
        tempp = np.where(tempp > 3,tempp - 3,tempp)
        yy[i - 1,:] = tempp.reshape(1,int(m/K))
        #print(yy[i - 1])
    #print(yy)
    
    ay = np.concatenate((y[k * 5:k * 5 + 5],y[k * 5+50:k * 5 + 5 + 50],y[k * 5 + 100:k * 5 + 5+ 100]), axis = 0)
    for i in range(int(m/K)): 
        tyy = yy[:,i].flatten()
        tyy = tyy.astype(int)
        count = np.bincount(tyy)
        ypred = np.argmax(count)
        #print(ypred)
        error = error +  np.sum(ypred != ay[i])
print(error)

