import bingo
tableros, numeros, marcados = bingo.tableros(), bingo.numeros(), []

def tableroCheck(iTablero, iRow, index) -> bool:
  checkRow, checkColumn = [], []
  for i in range(5):
    checkRow.append(str(iTablero)+'-'+str(iRow)+'-'+str(i))
    checkColumn.append(str(iTablero)+'-'+str(i)+'-'+str(index))
  if all(x in marcados for x in checkRow):
    return True
  if all(x in marcados for x in checkColumn):
    return True
  return False

def ganador(tab, numero):
  suma = 0
  for marcador in marcados:
    splitted = [int(i) for i in marcador.split('-')]
    tableros[splitted[0]][splitted[1]][splitted[2]] = 0
  
  for row in tableros[tab]:
    suma+=sum(row)

  print('Res=> ' + str(numero*suma))
  quit()

def letsPlay():
  i = 0
  for numero in numeros:
    iTab=0
    for tablero in tableros:
      iRow = 0
      for row in tablero:
        if numero in row:
          marcados.append(str(iTab)+ '-' + str(iRow) + '-' + str(row.index(numero)))
          if tableroCheck(iTab, iRow, row.index(numero)):
            ganador(iTab, numero)
        iRow+=1
      iTab+=1
    i+=1

letsPlay()