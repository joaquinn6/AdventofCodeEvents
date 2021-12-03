import informe

class reto2:

  def read_line(self, indice) -> dict:
    print(indice)
    binarios = informe.informe()[indice]
    return binarios

  def main(self):
    i=0
    array = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    binario = self.read_line(i)
    while binario != '':
      splitted = list(binario)
      for j in range(len(splitted)-1):
        if splitted[j]=='1':
          array[j][0]+=1
        else:
          array[j][1]+=1
      i+=1
      binario = self.read_line(i)
    gamma = []
    epsilon = []
    for j in range(len(splitted)):
      if array[j][0] > array[j][1]:
        gamma.append(1)
        epsilon.append(0)
      else:
        gamma.append(0)
        epsilon.append(1)
    g=int(str(''.join(map(str, gamma))), 2)
    e = int(str(''.join(map(str, epsilon))), 2)
    result = g * e
    print('result=>' + str(result) )

reto=reto2()
reto.main()