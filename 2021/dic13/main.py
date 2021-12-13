import instructions
folds, dots = instructions.folds(), instructions.dots()

def countRepetidos():
    noRepetidos = []
    for dot in dots:
        if dot not in noRepetidos:
            noRepetidos.append(dot)
    return noRepetidos

def fold():
  if folds[0][0] == 'y':
    for dot in dots:
      if dot[1] > folds[0][1]:
        dot[1] -= (dot[1]- folds[0][1])*2
  if folds[0][0] == 'x':
    for dot in dots:
      if dot[0] > folds[0][1]:
        dot[0] -= (dot[0]-folds[0][1])*2
  
  print(len(countRepetidos()))
  
fold()