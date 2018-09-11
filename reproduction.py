from constants import Cmax, Cmin, nPop
from airfoil_Class import baby_airfoil
import random

def reproduction(Airfoil, gen, sigma, i, s):  
                     
    costs = []

    for t in range(len(Airfoil)):
        costs.append(Airfoil[t].cost)

    BestCost = max(costs)

    WorstCost = min(costs)

    ratio = (Airfoil[i].cost - WorstCost)/(BestCost - WorstCost)
    C = int(Cmin + (Cmax - Cmin)*ratio)
    print(Airfoil[i].cost)
    print(C)

    if C > 0:

        progeny = []

        for j in range(C):
        
            progeny.append(baby_airfoil(Airfoil[i], gen, s[0]))

            progeny[j].new(sigma)
            progeny[j].bspline()
            progeny[j].write()
            progeny[j].savefig()

                     
            s[0] += 1

        for j in range(C):

            progeny[j].xFoil()
            Airfoil.append(progeny[j])