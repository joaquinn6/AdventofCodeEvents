import lineas
lineas, puntos = lineas.prueba(), []

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
    if num1 <= num2:
        mayor, menor = num2, num1
    else:
        mayor, menor = num1, num2
    return menor, mayor+1

def makePoints(linea):
    if linea[0] == linea[2]:
      menor, mayor = menor_mayor(linea[1], linea[3])
      for i in range(menor, mayor):
        puntos.append(str(linea[0]) + ',' + str(i))
    elif linea[1] == linea[3]:
      menor, mayor = menor_mayor(linea[0], linea[2])
      for i in range(menor, mayor):
          puntos.append(str(i) + ',' + str(linea[3]))
    elif linea[0] == linea[3] and linea[2] == linea[1]:
      menor, mayor = menor_mayor(linea[1], linea[3])
      for i in range(menor, mayor):
        puntos.append(str(mayor-1-i) + ',' + str(i))
    elif linea[0] == linea[1] and linea[2] == linea[3]: 
      menor, mayor = menor_mayor(linea[0], linea[3])
      for i in range(menor, mayor):
        puntos.append(str(i) + ',' + str(i))
    elif (linea[0] == linea[1] or linea[2] == linea[3]): 
      menorX, mayorX = menor_mayor(linea[0], linea[2])
      resta = mayorX-1-menorX
      menorY, mayorY = menor_mayor(linea[1], linea[3])
      suma = menorY + resta
      if suma+1 == mayorY:
        for i in range(resta+1):
          valor = str(mayorX - i -1) + ',' + str(menorY + i)
          puntos.append(valor)
    else:
      menorX, mayorX = menor_mayor(linea[0], linea[2])
      resta1 = mayorX-1-menorX
      menorY, mayorY = menor_mayor(linea[1], linea[3])
      resta2 = mayorY-1-menorY
      if resta1 == resta2:
        for i in range(resta1+1):
          valor = str(menorX + i) + ',' + str(menorY + i)
          puntos.append(valor)
          
def main():
    for linea in lineas:
        makePoints(linea)
    print("Res=> " + str(countRepetidos()))


main()
