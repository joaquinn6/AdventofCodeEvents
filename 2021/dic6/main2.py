import peces
import math
peces = peces.peces()
pecesPerDia = [0,0,0,0,0,0,0,0,0]
new_peces = 0

def dias(cant):
    for i in range(len(peces)):
        pecesPerDia[peces[i]] +=1

    for i in range(cant):
        dia0=pecesPerDia[0]
        pecesPerDia[0] =pecesPerDia[1]
        pecesPerDia[1] =pecesPerDia[2]
        pecesPerDia[2] =pecesPerDia[3]
        pecesPerDia[3] =pecesPerDia[4]
        pecesPerDia[4] =pecesPerDia[5]
        pecesPerDia[5] =pecesPerDia[6]
        pecesPerDia[6] =pecesPerDia[7]
        pecesPerDia[7] =pecesPerDia[8]
        pecesPerDia[6] +=dia0
        pecesPerDia[8] =dia0

    print(pecesPerDia)
    print("RES => ", str(sum(pecesPerDia)))


dias(256)
