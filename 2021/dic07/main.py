import posiciones
inicial = posiciones.posiciones()
def calculando(actual):
  gas = 0
  for num in range(len(inicial)):
    gas += abs(inicial[num]-actual)
  return gas
def moviendo():
  best=1e9
  for num in range(max(inicial)+1):
    gasolina= calculando(num)
    best=  min(gasolina, best)
  print("Result => Gasolina: ", best)
moviendo()