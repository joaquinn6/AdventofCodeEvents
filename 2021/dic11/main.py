import pulpos
contador, pulpos, flashForStep = [0], pulpos.prueba(), []

def evaluando(y, x):
  if pulpos[y][x]==10 and (y,x):
    flashForStep.append((y,x))
    contador[0]+=1
    maxY, maxX = len(pulpos)-1, len(pulpos[0])-1
    if y == 0 and x == 0:
      if (y+1,x) not in flashForStep:
        pulpos[y+1][x]+=1
        evaluando(y+1,x)
      if ((y,x+1)) not in flashForStep:
        pulpos[y][x+1] +=1
        evaluando(y,x+1)
      if (y+1,x+1) not in flashForStep:
        pulpos[y+1][x+1]+=1        
        evaluando(y+1,x+1)
    elif y == maxY and x == maxX:
      if (y-1,x) not in flashForStep:
        pulpos[y-1][x]+=1
        evaluando(y-1,x)
      if (y,x-1) not in flashForStep:
        pulpos[y][x-1]+=1
        evaluando(y,x-1)
      if (y-1,x-1) not in flashForStep:
        pulpos[y-1][x-1]+=1
        evaluando(y-1,x-1)
    elif y == 0 and x == maxX:
      if (y+1,x) not in flashForStep:
        pulpos[y+1][x]+=1
        evaluando(y+1,x)
      if (y,x-1) not in flashForStep:
        pulpos[y][x-1]+=1
        evaluando(y,x-1)
      if (y+1,x-1) not in flashForStep:
        pulpos[y+1][x-1]+=1
        evaluando(y+1,x-1)
    elif y == maxY and x == 0:
      if (y-1,x) not in flashForStep:
        pulpos[y-1][x]+=1
        evaluando(y-1,x)
      if (y,x+1) not in flashForStep:
        pulpos[y][x+1]+=1
        evaluando(y,x+1)
      if (y-1,x+1) not in flashForStep:
        pulpos[y-1][x+1]+=1
        evaluando(y-1,x+1)
    elif y == 0:
      if (y+1,x) not in flashForStep:
        pulpos[y+1][x]+=1
        evaluando(y+1,x)
      if (y+1,x+1) not in flashForStep:
        pulpos[y+1][x+1]+=1
        evaluando(y+1,x+1)
      if (y+1,x-1) not in flashForStep:
        pulpos[y+1][x-1]+=1
        evaluando(y+1,x-1)
      if (y,x+1) not in flashForStep:
        pulpos[y][x+1]+=1
        evaluando(y,x+1)
      if (y,x-1) not in flashForStep:
        pulpos[y][x-1]+=1
        evaluando(y,x-1)
    elif x == 0:
      if (y+1,x) not in flashForStep:
        pulpos[y+1][x]+=1
        evaluando(y+1,x)
      if (y-1,x) not in flashForStep:
        pulpos[y-1][x]+=1
        evaluando(y-1,x)
      if (y,x+1) not in flashForStep:
        pulpos[y][x+1]+=1
        evaluando(y,x+1)
      if (y+1,x+1) not in flashForStep:
        pulpos[y+1][x+1]+=1
        evaluando(y+1,x+1)
      if (y-1,x+1) not in flashForStep:
        pulpos[y-1][x+1]+=1
        evaluando(y-1,x+1)
    elif y == maxY:
      if (y-1,x) not in flashForStep:
        pulpos[y-1][x]+=1
        evaluando(y-1,x)
      if (y-1,x-1) not in flashForStep:
        pulpos[y-1][x-1]+=1
        evaluando(y-1,x-1)
      if (y-1,x+1) not in flashForStep:
        pulpos[y-1][x+1]+=1
        evaluando(y-1,x+1)
      if (y,x-1) not in flashForStep:
        pulpos[y][x-1]+=1
        evaluando(y,x-1)
      if (y,x+1) not in flashForStep:
        pulpos[y][x+1]+=1
        evaluando(y,x+1)
    elif x == maxX:
      if (y,x-1) not in flashForStep:
        pulpos[y][x-1]+=1
        evaluando(y,x-1)
      if (y-1,x-1) not in flashForStep:
        pulpos[y-1][x-1]+=1
        evaluando(y-1,x-1)
      if (y+1,x-1) not in flashForStep:
        pulpos[y+1][x-1]+=1
        evaluando(y+1,x-1)
      if (y-1,x) not in flashForStep:
        pulpos[y-1][x]+=1
        evaluando(y-1,x)
      if (y+1,x) not in flashForStep:
        pulpos[y+1][x]+=1
        evaluando(y+1,x)
    else:
      if (y+1,x-1) not in flashForStep:
        pulpos[y+1][x-1]+=1
        evaluando(y+1,x-1)
      if (y+1,x) not in flashForStep:
        pulpos[y+1][x]+=1
        evaluando(y+1,x)
      if (y+1,x+1) not in flashForStep:
        pulpos[y+1][x+1]+=1
        evaluando(y+1,x+1)
      if (y-1,x-1) not in flashForStep:
        pulpos[y-1][x-1]+=1
        evaluando(y-1,x-1)
      if (y-1,x) not in flashForStep:
        pulpos[y-1][x]+=1
        evaluando(y-1,x)
      if (y-1,x+1) not in flashForStep:
        pulpos[y-1][x+1]+=1
        evaluando(y-1,x+1)
      if (y,x-1) not in flashForStep:
        pulpos[y][x-1]+=1
        evaluando(y,x-1)
      if (y,x+1) not in flashForStep:
        pulpos[y][x+1]+=1
        evaluando(y,x+1)

def make0():
  for tupla in flashForStep:
    pulpos[tupla[0]][tupla[1]]=0

def steps():
  for step in range(100):
    make0()
    flashForStep.clear()
    print(step)
    for y in range(10):
      for x in range(10):
        pulpos[y][x]+=1
        evaluando(y,x)
  print(contador)

steps()