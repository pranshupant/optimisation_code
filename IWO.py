from constants import maxIt, Gen0, sigma_final, sigma_initial, exponent, nPop
from airfoil_Class import airfoil, baby_airfoil
import subprocess as sp
import os
import numpy as np
from reproduction import reproduction

Airfoil = []
st = [0]
s = np.array(st)

for i in range(Gen0):
    
    Airfoil.append(airfoil(0,i))
    Airfoil[i].ctrlPoints()
    Airfoil[i].bspline()
    Airfoil[i].write()

for i in range(Gen0):
    #Airfoil[i].savefig()
    Airfoil[i].xFoil()
    #Airfoil[i].cfd()
    print(Airfoil[i].cost)

    gen = 1

if __name__ == "__main__":

    while gen < maxIt:

        sigma = (((maxIt - float(i))/(maxIt - 1))**exponent)*(sigma_initial - sigma_final) + sigma_final

        for x in range(len(Airfoil)):
            reproduction(Airfoil, gen, sigma, x, s)      

        Airfoil.sort(key = lambda x: x.cost, reverse = True)

        for i in range(len(Airfoil)):
            print(Airfoil[i].cost)

        del Airfoil[nPop:]

        gen += 1 
        s[0] = 0
     

        