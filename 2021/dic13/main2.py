import instructions
folds, dots = instructions.folds(), instructions.dots()

def eliminarRepetidos():
    noRepetidos = []
    for dot in dots:
        if dot not in noRepetidos:
            noRepetidos.append(dot)
    return noRepetidos

def maximos(puntos):
  y, x=0,0
  for punto in puntos:
    y = punto[0] if punto[0]>y else y
    x = punto[1] if punto[1]>x else x
  return y, x
  
def draw(puntos):
  puntoYMax, puntoXMax = maximos(puntos)
  outputStr = ''
  for x in range(puntoXMax+1):
    for y in range(puntoYMax+1):
      outputStr +='#' if [y,x] in puntos else '.'
    outputStr += '\n'
  print (outputStr)

def fold():
  for fold in folds:
    if fold[0] == 'y':
      for dot in dots:
          dot[1] -= (dot[1]- fold[1])*2 if dot[1] > fold[1] else 0
    if fold[0] == 'x':
      for dot in dots:
          dot[0] -= (dot[0]-fold[1])*2 if dot[0] > fold[1] else 0
  draw(eliminarRepetidos())
  
fold()