import lineas
lineas, puntos = lineas.lineas(), []

def countRepetidos():
    repetidos, unicos = [], []
    for punto in puntos:
        if punto not in unicos:
            unicos.append(punto)
        elif punto not in repetidos:
            repetidos.append(punto)
    return len(repetidos)

def menor_mayor(num1, num2):
    mayor, menor = 0, 0
    if num1 < num2:
        mayor, menor = num2, num1
    else:
        mayor, menor = num1, num2
    return range(menor, mayor+1)

def makePoints(linea):
    if linea[0] == linea[2]:
        for i in menor_mayor(linea[1], linea[3]):
            puntos.append(str(linea[0]) + ',' + str(i))
    elif linea[1] == linea[3]:
        for i in menor_mayor(linea[0], linea[2]):
            puntos.append(str(i) + ',' + str(linea[3]))

def main():
    for linea in lineas:
        makePoints(linea)
    print("Res=> " + str(countRepetidos()))

main()
