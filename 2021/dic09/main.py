import cuevas
cuevas, mediciones = [],cuevas.cuevas() 
for medicion in mediciones:
  cuevas.append([int(x) for x in list(medicion)])

def calculandoRuta():
  contador, maxI, maxJ=0, len(cuevas)-1, len(cuevas[0])-1
  for i in range(len(cuevas)):
    for j in range(len(cuevas[i])):
      if i==0 and j==0:
        if cuevas[i][j] < min(cuevas[i+1][j],cuevas[i][j+1]):
          contador += cuevas[i][j]+1
      elif i==maxI and j==maxJ:
        if cuevas[i][j] < min(cuevas[i-1][j],cuevas[i][j-1]):
          contador += cuevas[i][j]+1
      elif i==0 and j==maxJ:
        if cuevas[i][j] < min(cuevas[i+1][j],cuevas[i][j-1]):
          contador += cuevas[i][j]+1
      elif i==maxI and j==0:
        if cuevas[i][j] < min(cuevas[i-1][j],cuevas[i][j-1]):
          contador += cuevas[i][j]+1
      elif i==0:
        if cuevas[i][j] < min(cuevas[i+1][j],cuevas[i][j+1], cuevas[i][j-1]):
          contador += cuevas[i][j]+1
      elif j==0:
        if cuevas[i][j] < min(cuevas[i+1][j],cuevas[i][j+1], cuevas[i-1][j]):
          contador += cuevas[i][j]+1
      elif i==maxI:
        if cuevas[i][j] < min(cuevas[i-1][j],cuevas[i][j+1], cuevas[i][j-1]):
          contador += cuevas[i][j]+1
      elif j==maxJ:
        if cuevas[i][j] < min(cuevas[i+1][j],cuevas[i][j-1], cuevas[i-1][j]):
          contador += cuevas[i][j]+1
      else:
        if cuevas[i][j] < min(cuevas[i+1][j],cuevas[i-1][j],cuevas[i][j-1], cuevas[i][j+1]):
          contador += cuevas[i][j]+1
  print(contador)

calculandoRuta()
