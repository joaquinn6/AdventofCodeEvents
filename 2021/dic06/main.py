import peces
peces = peces.peces()

def dias(cant):
    for i in range(cant):
        cantidad = len(peces)
        for i in range(cantidad):
            peces[i] -= 1
            if peces[i] == -1:
                peces[i] = 6
                peces.append(8)
    print("RES => ", str(len(peces)))

dias(80)
