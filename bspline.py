import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import random
import stl
from stl import mesh
from stl_gen import STL_Gen

LB = 0.05
UB = 0.2

LB2 = -0.1
UB2 = 0.1

yp = []
yl = []
plist = np.zeros((9,2))
ulist = np.zeros((9,2))

for rand in range(7):
    yl.append(random.uniform(LB2, UB2))

ulist[1] = [0, random.uniform(-0.1, 0)]
ulist[8] = [1, 0]

for i in range(2, 8):
    ulist[i][0] = 0.1*(i-1)
    ulist[i][1] = yl[i-2]

for rand in range(7):
    yp.append(random.uniform(yl[rand] + 0.1,  UB))

plist[1] = [0, random.uniform(0, 0.2)]
plist[8] = [1, 0]

for i in range(2, 8):
    plist[i][0] = 0.1*(i-1)
    plist[i][1] = yp[i-2]



#print(ulist)
#print(plist)


ctr = np.array(plist)
ltr = np.array(ulist)

x = ctr[:,0]
y = ctr[:,1]

x1 = ltr[:,0]
y1 = ltr[:,1]


l=len(x)
t=np.linspace(0,1,l-2,endpoint=True)
t=np.append([0,0,0],t)
t=np.append(t,[1,1,1])

tck=[t,[x,y],3]
lck=[t,[x1,y1],3]
u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
out = interpolate.splev(u3,tck) 
out1 = interpolate.splev(u3,lck) 

#print(len(out1[0]))

plt.plot(x,y,'k--',label='Control polygon',marker='o',markerfacecolor='red')
plt.plot(out[0],out[1],'b',linewidth=2.0,label='B-spline curve')

plt.plot(x1,y1,'k--',label='Control polygon',marker='o',markerfacecolor='red')
plt.plot(out1[0],out1[1],'b',linewidth=2.0,label='B-spline curve')

plt.legend(loc='best')
plt.axis([min(x)-0.1, max(x)+0.1, min(y)-1, max(y)+1])
plt.title('Cubic B-spline curve evaluation')
plt.show()

coors=[]

X1=np.array(out[0])
X2=np.array(out1[0])
X3=X2[: : -1]

X=np.concatenate((X1,X3), 0)

Y1=np.array(out[1])
Y2=np.array(out1[1])
Y3=Y2[: : -1]

Y=np.concatenate((Y1,Y3), 0)
#print(X3)

STL_Gen(X,Y,1)


for j in range(len(out[0])):
    coors.append([out[0][j], out[1][j]])

#print(coors)
coors.reverse()

for k in range(1, len(out1[0])):
    coors.append([out1[0][k], out1[1][k]])

f = open("../bspline-xfoil/bsairfoil.txt", "w")
f.write('BSA') 
f.write('\n')

for i in range(len(out[0])*2 - 1):
   
    str1 = str(coors[i]).strip('[]')
    f.write(str1.strip(','))
    f.write('\n')

f.close()

