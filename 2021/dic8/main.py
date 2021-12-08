counter=0
with open("values.txt","r") as archivo:
  for linea in archivo:
    arrayOutputs= linea.split('|')[1].strip().split(" ")
    for comando in arrayOutputs:
      if len(comando) in [2,4,3,7]:
        counter+=1
print (counter)