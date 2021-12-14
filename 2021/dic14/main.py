import polimeros
polimero, rules= polimeros.inicio(), polimeros.rules()

for i in range(10):
  copyPol= polimero[0] 
  for j in range(1, len(polimero)):
    insertBtw = rules[polimero[j-1]+polimero[j]]
    copyPol += insertBtw + polimero[j]
  polimero=copyPol

unicos=[]
for i in range(len(polimero)):
  if polimero[i] not in unicos:
    unicos.append(polimero[i])
mayor =0
menor =2e9
for i in range(len(unicos)):
  cant = polimero.count(unicos[i])
  mayor = cant if cant > mayor else mayor
  menor = cant if cant < menor else menor 

print(mayor-menor)