
import cuevas
cuevas, mediciones, maxI, maxJ = [], cuevas.cuevas(), 0, 0
for medicion in mediciones:
    cuevas.append([int(x) for x in list(medicion)])


def inicioCalculo(i, j):
    allTuplas, tuplas = [[i, j]], []
    tuplas.append([i, j])
    while len(tuplas) > 0:
        copyTuplas = tuplas[:]
        tuplas.clear()
        for tup in copyTuplas:
            tuplas += calcularCuencas(tup[0], tup[1], allTuplas)
        allTuplas += tuplas[:]
    return allTuplas

def calcularCuencas(i, j, allTuplas):
    tuplas, maxI, maxJ = [], len(cuevas)-1, len(cuevas[0])-1
    if i == 0 and j == 0:
        if cuevas[i+1][j] != 9 and [i+1, j] not in allTuplas and [i+1, j] not in tuplas:
            tuplas.append([i+1, j])
        if cuevas[i][j+1] != 9 and [i, j+1] not in allTuplas and [i, j+1] not in tuplas:
            tuplas.append([i, j+1])
    elif i == maxI and j == maxJ:
        if cuevas[i-1][j] != 9 and [i-1, j] not in allTuplas and [i-1, j] not in tuplas:
            tuplas.append([i-1, j])
        if cuevas[i][j-1] != 9 and [i, j-1] not in allTuplas and [i, j-1] not in tuplas:
            tuplas.append([i, j-1])
    elif i == 0 and j == maxJ:
        if cuevas[i+1][j] != 9 and [i+1, j] not in allTuplas and [i+1, j] not in tuplas:
            tuplas.append([i+1, j])
        if cuevas[i][j-1] != 9 and [i, j-1] not in allTuplas and [i, j-1] not in tuplas:
            tuplas.append([i, j-1])
    elif i == maxI and j == 0:
        if cuevas[i-1][j] != 9 and [i-1, j] not in allTuplas and [i-1, j] not in tuplas:
            tuplas.append([i-1, j])
        if cuevas[i][j+1] != 9 and [i, j+1] not in allTuplas and [i, j+1] not in tuplas:
            tuplas.append([i, j+1])
    elif i == 0:
        if cuevas[i+1][j] != 9 and [i+1, j] not in allTuplas and [i+1, j] not in tuplas:
            tuplas.append([i+1, j])
        if cuevas[i][j+1] != 9 and [i, j+1] not in allTuplas and [i, j+1] not in tuplas:
            tuplas.append([i, j+1])
        if cuevas[i][j-1] != 9 and [i, j-1] not in allTuplas and [i, j-1] not in tuplas:
            tuplas.append([i, j-1])
    elif j == 0:
        if cuevas[i+1][j] != 9 and [i+1, j] not in allTuplas and [i+1, j] not in tuplas:
            tuplas.append([i+1, j])
        if cuevas[i][j+1] != 9 and [i, j+1] not in allTuplas and [i, j+1] not in tuplas:
            tuplas.append([i, j+1])
        if cuevas[i-1][j] != 9 and [i-1, j] not in allTuplas and [i-1, j] not in tuplas:
            tuplas.append([i-1, j])
    elif i == maxI:
        if cuevas[i-1][j] != 9 and [i-1, j] not in allTuplas and [i-1, j] not in tuplas:
            tuplas.append([i-1, j])
        if cuevas[i][j+1] != 9 and [i, j+1] not in allTuplas and [i, j+1] not in tuplas:
            tuplas.append([i, j+1])
        if cuevas[i][j-1] != 9 and [i, j-1] not in allTuplas and [i, j-1] not in tuplas:
            tuplas.append([i, j-1])
    elif j == maxJ:
        if cuevas[i+1][j] != 9 and [i+1, j] not in allTuplas and [i+1, j] not in tuplas:
            tuplas.append([i+1, j])
        if cuevas[i][j-1] != 9 and [i, j-1] not in allTuplas and [i, j-1] not in tuplas:
            tuplas.append([i, j-1])
        if cuevas[i-1][j] != 9 and [i-1, j] not in allTuplas and [i-1, j] not in tuplas:
            tuplas.append([i-1, j])
    else:
        if cuevas[i+1][j] != 9 and [i+1, j] not in allTuplas and [i+1, j] not in tuplas:
            tuplas.append([i+1, j])
        if cuevas[i-1][j] != 9 and [i-1, j] not in allTuplas and [i-1, j] not in tuplas:
            tuplas.append([i-1, j])
        if cuevas[i][j-1] != 9 and [i, j-1] not in allTuplas and [i, j-1] not in tuplas:
            tuplas.append([i, j-1])
        if cuevas[i][j+1] != 9 and [i, j+1] not in allTuplas and [i, j+1] not in tuplas:
            tuplas.append([i, j+1])
    return tuplas

def limpiarLista(lista):
    newLista=[]
    for item in lista:
        if item not in newLista:
            newLista.append(item)
    return newLista

def calculandoRuta():
    contador, maxI, maxJ = [], len(cuevas)-1, len(cuevas[0])-1
    for i in range(len(cuevas)):
        for j in range(len(cuevas[i])):
            if i == 0 and j == 0:
                if cuevas[i][j] < min(cuevas[i+1][j], cuevas[i][j+1]):
                    lista=limpiarLista(inicioCalculo(i, j))
                    contador.append(len(lista))
            elif i == maxI and j == maxJ:
                if cuevas[i][j] < min(cuevas[i-1][j], cuevas[i][j-1]):
                    lista=limpiarLista(inicioCalculo(i, j))
                    contador.append(len(lista))
            elif i == 0 and j == maxJ:
                if cuevas[i][j] < min(cuevas[i+1][j], cuevas[i][j-1]):
                    lista=limpiarLista(inicioCalculo(i, j))
                    contador.append(len(lista))
            elif i == maxI and j == 0:
                if cuevas[i][j] < min(cuevas[i-1][j], cuevas[i][j-1]):
                    lista=limpiarLista(inicioCalculo(i, j))
                    contador.append(len(lista))
            elif i == 0:
                if cuevas[i][j] < min(cuevas[i+1][j], cuevas[i][j+1], cuevas[i][j-1]):
                    lista=(limpiarLista(inicioCalculo(i, j)))
                    contador.append(len(lista))
            elif j == 0:
                if cuevas[i][j] < min(cuevas[i+1][j], cuevas[i][j+1], cuevas[i-1][j]):
                    lista=limpiarLista(inicioCalculo(i, j))
                    contador.append(len(lista))
            elif i == maxI:
                if cuevas[i][j] < min(cuevas[i-1][j], cuevas[i][j+1], cuevas[i][j-1]):
                    lista=limpiarLista(inicioCalculo(i, j))
                    contador.append(len(lista))
            elif j == maxJ:
                if cuevas[i][j] < min(cuevas[i+1][j], cuevas[i][j-1], cuevas[i-1][j]):
                    lista=limpiarLista(inicioCalculo(i, j))
                    contador.append(len(lista))
            else:
                if cuevas[i][j] < min(cuevas[i+1][j], cuevas[i-1][j], cuevas[i][j-1], cuevas[i][j+1]):
                    lista=limpiarLista(inicioCalculo(i, j))
                    contador.append(len(lista))
    contador.sort()
    multi=contador[len(contador)-1]*contador[len(contador)-2]*contador[len(contador)-3]
    print(multi)


calculandoRuta()
