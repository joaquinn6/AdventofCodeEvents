import ordenes
i,x,y,aim=0,0,0,0
orden = ordenes.ordenes()[i]
while orden['direction']!='exit':
  if (orden['direction']=='down'):
    aim+=orden['num']
  if (orden['direction']=='up'):
    aim-=orden['num']
  if (orden['direction']=='forward'):
    x+=orden['num']
    y+=orden['num']*aim
  i+=1
  orden = ordenes.ordenes()[i]
print('result=>' + str(x*y))
