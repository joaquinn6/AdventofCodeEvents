import posiciones
inicial = posiciones.prueba()

def calculando(actual):
  gasTotal = 0
  for num in range(len(inicial)):
    gas = abs(inicial[num]- actual)
    gasTotal+=sum(range(gas+1))
  return gasTotal
def moviendo():
  best=1e9
  inicial.sort()
  for num in range(inicial[len(inicial)-1]+1):
    gasolina= calculando(num)
    best= gasolina if gasolina < best else best
  print("Result => Gasolina: ", best)

moviendo()