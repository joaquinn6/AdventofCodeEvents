import posiciones
inicial = posiciones.posiciones()

def mayor_menos_menor(num1, num2):
    mayor, menor = 0, 0
    if num1 < num2:
        mayor, menor = num2, num1
    else:
        mayor, menor = num1, num2
    return mayor-menor

def calculando(actual):
  gas = 0
  for num in range(len(inicial)):
    gas += mayor_menos_menor(inicial[num], actual)
  return gas

def moviendo():
  best, best_position =10000000000000, inicial[0]
  inicial.sort()
  for num in range(inicial[len(inicial)-1]+1):
    gasolina= calculando(num)
    if gasolina < best:
      best_position= num
      best= gasolina
  print("Result => Posición: ", best_position, " Gasolina: ", best)

moviendo()