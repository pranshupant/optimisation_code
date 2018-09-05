import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import random
import stl
from stl import mesh
from stl_gen import STL_Gen
import subprocess as sp
import shutil
import sys
import string
import re
import os

class airfoil():
    def __init__(self):
        
        self.uPoint = np.zeros((5,2))
        self.lPoint = np.zeros((5,2))
        self.plotX = []
        self.plotY = []
        self.cost = 0.0

    def bspline(self): #Import bspline.py

        LBY = 0.05 # Upper Array
        UBY = 0.2

        LBY2 = -0.1 # Lower Array
        UBY2 = 0.1

        LBX = 0.1
        UBX = 0.8

        
        self.uPoint[1] = [0, random.uniform(-0.1, -0.05)] # Lower Array
        self.uPoint[4] = [1, 0]

        for i in range(2, 4):
            self.uPoint[i][0] = random.uniform((LBX if (i==2) else self.uPoint[2][0]+0.1),
                                         (0.4 if (i==2) else UBX))
            self.uPoint[i][1] = random.uniform(LBY2, UBY2)

        self.lPoint[1] = [0, random.uniform(0.05, 0.2)] # Upper Array
        self.lPoint[4] = [1, 0]

        for i in range(2, 4):
            self.lPoint[i][0] = random.uniform((LBX if (i==2) else self.lPoint[2][0]+0.1),
                                         (0.4 if (i==2) else UBX))
            self.lPoint[i][1] = random.uniform(LBY if (LBY>self.uPoint[i][1]) 
                                             else self.uPoint[i][1]+0.1, UBY)

        #print(self.uPoint)
        #print(self.lPoint)


        ctr = np.array(self.lPoint)
        ltr = np.array(self.uPoint)

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
        
        X1=np.array(out[0])
        X2=np.array(out1[0])
        X3=X2[: : -1]

        X=np.concatenate((X1,X3), 0)
        self.plotX = X

        Y1=np.array(out[1])
        Y2=np.array(out1[1])
        Y3=Y2[: : -1]

        Y=np.concatenate((Y1,Y3), 0)
        self.plotY = Y

        STL_Gen(X,Y,1)

    def xFoil(self):    #Extraction of L/d done
        sp.Popen(['xfoil <controlfile.xfoil>outputfile.out'],
         stdin=sp.PIPE,
         stdout=None,
         stderr=None,
         shell=True
         )
        while 1:
            if os.path.isfile("bsx.txt"):        
                f = open("bsx.txt", "r")
                for line in f:
                    line = f.read()
                break

        p = re.findall('\s+[.\d]{5}\s+([.\d]{6})\s+([.\d]{6})', line)

        r = float(p[0][0])/float(p[0][1])

        self.cost = r
        
    def cfd(self):  #Extract result from post processing

        f = open("/home/pranshu/Desktop/openFoam/2D_SImpleFoamWing_1/postProcessing/forceCoeffs1/0/forceCoeffs.dat", "r")
        for line in f:
             line = f.read()

        p = re.findall('999\s+([-.A-Za-z0-9]+)\s+([-.A-Za-z0-9]+)', line)

        r = float(p[0][0])/float(p[0][1])

        self.cost = r

    def reproduce(self):

        print("1")

    def show(self):   #display using matplotlib

        plt.plot(self.uPoint[:,0], self.uPoint[:,1],'k--',label='Control polygon',marker='o',markerfacecolor='red')
       
        plt.plot(self.lPoint[:,0],self.lPoint[:,1],'k--',label='Control polygon',marker='o',markerfacecolor='green')
       
        plt.plot(self.plotX, self.plotY,'b',linewidth=2.0,label='B-spline curve')
        
        plt.legend(loc='best')
        plt.axis([min(self.plotX)-0.1, max(self.plotX)+0.1, min(self.plotY)-0.5, max(self.plotY)+0.5])
        plt.title('Cubic B-spline curve evaluation')
        plt.show()