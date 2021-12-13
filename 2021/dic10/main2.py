counter, arrayOutputs =[], [],
    
with open("2021/dic10/navigation.txt","r") as archivo:
  for linea in archivo:
    arrayOutputs.append(list(linea.strip()))

def sacandoTotal(openTags):
  total=0
  reverseTags = openTags[::-1]
  for tag in reverseTags:
    total *= 5
    if tag=='(':
      total+=1
    if tag=='[':
      total+=2
    if tag=='{':
      total+=3
    if tag=='<':
      total+=4
  counter.append(total)
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
          exit=False
        elif arrayOutputs[i][cont] == ')' and expected[len(expected)-1] in ['<', '[', '{']:
          exit=False
        elif arrayOutputs[i][cont] == '>' and expected[len(expected)-1] in ['{', '[', '(']:
          exit=False
        elif arrayOutputs[i][cont] == ']' and expected[len(expected)-1] in ['<', '{', '(']:
          exit=False
        else:
          expected.pop(len(expected)-1)
      if cont == len(arrayOutputs[i])-1 and exit:
        sacandoTotal(expected)
      if cont == len(arrayOutputs[i])-1:
        exit=False
      
      cont +=1
  counter.sort()
  mitad = int(len(counter) / 2)
  print(counter[mitad])

findErrors()