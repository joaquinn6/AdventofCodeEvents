counter, arrayOutputs =[0,0,0,0], [],
    
with open("2021/dic10/navigation.txt","r") as archivo:
  for linea in archivo:
    arrayOutputs.append(list(linea.strip()))

def sumandoError(closeTag):
  if closeTag==')':
    counter[0]+=3
  if closeTag==']':
    counter[1]+=57
  if closeTag=='}':
    counter[2]+=1197
  if closeTag=='>':
    counter[3]+=25137
def findErrors():
  for i in range(len(arrayOutputs)):
    exit = True
    cont = 0
    expected = []
    while exit:
      if arrayOutputs[i][cont] in ['<','{', '[', '(']:
        expected.append(arrayOutputs[i][cont])
      else:
        if arrayOutputs[i][cont] == '}' and expected[len(expected)-1] in ['<', '[', '(']:
          sumandoError(arrayOutputs[i][cont])
          exit=False
        elif arrayOutputs[i][cont] == ')' and expected[len(expected)-1] in ['<', '[', '{']:
          sumandoError(arrayOutputs[i][cont])
          exit=False
        elif arrayOutputs[i][cont] == '>' and expected[len(expected)-1] in ['{', '[', '(']:
          sumandoError(arrayOutputs[i][cont])
          exit=False
        elif arrayOutputs[i][cont] == ']' and expected[len(expected)-1] in ['<', '{', '(']:
          sumandoError(arrayOutputs[i][cont])
          exit=False
        else:
          expected.pop(len(expected)-1)
      if cont == len(arrayOutputs[i])-1:
        exit=False 
      cont +=1
  print(sum(counter))

findErrors()