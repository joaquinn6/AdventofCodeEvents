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


def makePoints(linea):
  mayor, menor=0,0
  if linea[0] == linea[2]:
    if linea[1] < linea[3]:
      mayor, menor = linea[3], linea[1]
    else:
      mayor, menor = linea[1], linea[3]
    for i in range(menor, mayor+1):
      puntos.append(str(linea[0]) + ',' + str(i))
  if linea[1]== linea[3]:
    if linea[0] < linea[2]:
      mayor, menor = linea[2], linea[0]
    else:
      mayor, menor = linea[0], linea[2]
    for i in range(menor, mayor+1):
      puntos.append(str(i) +','+ str(linea[3]))

def main():
  for linea in lineas:
    makePoints(linea)
  print("Res=> " + str(countRepetidos())) 

main()