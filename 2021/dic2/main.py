import ordenes

class reto2:

  def read_line(self, indice) -> dict:
    print(indice)
    orden = ordenes.ordenes()[indice]
    return orden

  def main(self):
    i=0
    x=0
    y=0
    aim=0
    orden = self.read_line(i)
    while orden['direction']!='exit':
      if (orden['direction']=='down'):
        aim+=orden['num']
      if (orden['direction']=='up'):
        aim-=orden['num']
      if (orden['direction']=='forward'):
        x+=orden['num']
        y+=orden['num']*aim
      i+=1
      orden = self.read_line(i)
    print('result=>' + str(x*y))

reto=reto2()
reto.main()