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
    # Valido si X Y 1 tienen la misma diferencia con X Y 2 respectivamente
    elif (linea[0]>linea[2] and linea[1]>linea[3]) or (linea[0]<linea[2] and linea[1]<linea[3]):
      menor1, mayor1 = menor_mayor(linea[0], linea[2])
      menor2, mayor2 = menor_mayor(linea[1], linea[3])
      resta1 = mayor1 - menor1
      resta2 = mayor2 - menor2
      if resta1==resta2:
        for i in range(resta2):
          puntos.append(str(menor1+i) + ',' + str(menor2+i))
    else:
      menor1, mayor1 = menor_mayor(linea[0], linea[2])
      menor2, mayor2 = menor_mayor(linea[1], linea[3])
      resta = mayor1 - menor1
      suma = resta+menor2
      if suma == mayor2:
        if linea[0]+1 == mayor1:
          for i in range(resta):
            valor = str(mayor1-i-1) + ',' + str(menor2 + i)
            puntos.append(valor)
        else:
          for i in range(resta):
            valor = str(menor1 + i) + ',' + str(mayor2-i-1)
            puntos.append(valor)
def main():
    for linea in lineas:
        makePoints(linea)
    print("Res=> " + str(countRepetidos()))


main()
