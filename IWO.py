from constants import maxIt, Gen0, sigma_final, sigma_initial, exponent, nPop
from airfoil_Class import airfoil
import subprocess as sp
import os
from reproduction import reproduction

Airfoil = []

for i in range(Gen0):
    
    Airfoil.append(airfoil(0,i))
    Airfoil[i].ctrlPoints()
    Airfoil[i].bspline()
    Airfoil[i].write()
    #Airfoil[i].savefig()
    Airfoil[i].xFoil()
    Airfoil[i].cfd()

if __name__ == "__main__":

    gen = 1

    while gen < maxIt:

        sigma = (((maxIt - float(i))/(maxIt - 1))**exponent)*(sigma_initial - sigma_final) + sigma_final

        for x in range(len(Airfoil)):
            reproduction(Airfoil, gen, sigma, x)      

        Airfoil.sort(key = lambda x: x.cost)

        del Airfoil[nPop:]

        gen += 1 
        s = 0

        

        