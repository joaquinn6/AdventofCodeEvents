import informe
class reto3:
  def resultado(self, array) -> int:
    gamma, epsilon = [], []
    for j in range(12):
      if array[j][0] > array[j][1]:
        gamma.append(1)
        epsilon.append(0)
      else:
        gamma.append(0)
        epsilon.append(1)
    return int(str(''.join(map(str, gamma))), 2) * int(str(''.join(map(str, epsilon))), 2)

  def main(self):
    i, array = 0, [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    binario = informe.informe()[i]
    while binario != '':
      splitted = list(binario)
      for j in range(len(splitted)-1):
        if splitted[j]=='1':
          array[j][0]+=1
        else:
          array[j][1]+=1
      i+=1
      binario = informe.informe()[i]
    result = self.resultado(array)
    print('result=>' + str(result))
reto=reto3()
reto.main()