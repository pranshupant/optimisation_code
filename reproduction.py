from constants import Cmax, Cmin 

def reproduction(Airfoil, gen, sigma, i):  
                        
    global s

    costs = []

    for t in range(len(Airfoil)):
        costs.append(Airfoil[t].cost)

    BestCost = min(costs)

    WorstCost = max(costs)

    ratio = (Airfoil[i].Cost - WorstCost)/(BestCost - WorstCost)
    C = int(Cmin + (Cmax - Cmin)*ratio)

    if C > 0:

        for j in range(C):

            Airfoil[j].new(gen, s, sigma)
            Airfoil[j].bspline()
            Airfoil[j].write()
            Airfoil[j].xFoil()
            s += 1
