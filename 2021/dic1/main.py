import medidas
class reto1:
  def compare(self, array) -> bool:
    suma1 = array[0]+ array[1] + array[2]
    suma2 = array[3]+ array[1] + array[2]
    if (suma2>suma1):
      return True
    return False
  def main(self):
    i, aceleracion, medida, array=0, 0, 1, []
    while medida!=0:
      if(len(array)==4):
        if (self.compare(array)):
          aceleracion +=1
      medida = medidas.medidas()[i]
      array.append(medida)
      if (len(array)>4):
        array.pop(0)
      i+=1
    print('result=>' + str(aceleracion))
reto=reto1()
reto.main()