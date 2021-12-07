import posiciones
inicial = posiciones.posiciones()
def calculando(actual):
  gas = 0
  for num in range(len(inicial)):
    gas += abs(inicial[num]-actual)
  return gas
def moviendo():
  best=1e9
  inicial.sort()
  for num in range(inicial[len(inicial)-1]+1):
    gasolina= calculando(num)
    best= gasolina if gasolina < best else best
  print("Result => Gasolina: ", best)
moviendo()