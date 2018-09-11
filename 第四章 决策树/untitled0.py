import numpy as np
import csv
d = 8#属性个数
m = 17#样例个数

f = csv.reader(open("watermelon3_0_Ch.csv","r"))
x = np.random.rand(m,d)
y = np.random.randn(m,1)
data = []
for line in f:
    data.append(line)
data = np.array(data)
x = data[1:,1:9]
y = data[1:,9].reshape(-1,1)
N = 20
a = []
for i in range(8):a.append(i)
node =[[] for i in range(N)]#node值表示属性编号
def fun(tx,ty,a):
    return a[0]
def TreeGenerate(tx,ty,a,deep):
    
    print("???")
    #node[deep].append()
    num = ty == "是"
    num = ty[num].size
    if (num == 0 or num == ty.size):
        if num == 0 : node[deep].append(-2)#否
        else : node[deep].append(-1)#是
        print(1)
        return
    if(len(a) == 0):
        if num < ty.size / 2 : node[deep].append(-2)#否
        else : node[deep].append(-1)#是
        print(2)
        return
    flag = False
    for line in a:
        temp = tx[:,line]
        mask  = (temp  == tx[0,line])
        tnum = temp[mask].size
        if(tnum != m):
            flag = True
    if(len(a) == 0 or flag == False):
        node[deep].append(-1)
        print(3)
        return
    aw = fun(tx,ty,a) 
    print(4)
  #  print(aw)
    for i in np.unique(tx[:,aw]):
        print(i)
        #print(tx)
        idx = np.where(tx[:,aw] == i)
        #print(idx)
        idx = idx[0]
        ttx = tx[idx,:]
        #print(ttx)
        tty = ty[idx,:]  
        #print(idx)
        if(len(idx) == 0):
            if num < tty.size / 2 : node[deep].append(-2)#否
            else : node[deep].append(-1)#是
            return
        else:
            ta = []
            if aw < 8:

                for i in range(len(a)):
                    if i != aw:
                        ta.append(i)
                print(ttx)
                #ttx = np.delete(ttx,aw,axis = 1)
                #print(ttx)
                print("!!!!!!!!!!!!!")
                print(ttx)
                print(ta)
                
            TreeGenerate(ttx,tty,ta,deep + 1)
    return
            
TreeGenerate(x,y,a,0)
        