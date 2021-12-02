import medidas

class reto1:

  def read_line(self, indice) -> int:
    print(indice)
    medida = medidas.medidas()[indice]
    return medida

  def compare(self, array) -> bool:
    suma1 = array[0]+ array[1] + array[2]
    suma2 = array[3]+ array[1] + array[2]
    if (suma2>suma1):
      return True
    return False

  def main(self):
    i=0
    array = []
    aceleracion=0
    medida = 1
    while medida!=0:
      if(len(array)==4):
        if (self.compare(array)):
          aceleracion +=1
      medida = self.read_line(i)
      array.append(medida)
      if (len(array)>4):
        array.pop(0)
      i+=1
    print('result=>' + str(aceleracion))

reto=reto1()
reto.main()