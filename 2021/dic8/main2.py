arrayOutputs = []
with open("/home/joaquin/Documentos/Personal/afcode/2021/dic8/values.txt", "r") as archivo:
    for linea in archivo:
        arrayOutputs.append(linea.split('|'))

def whichWith(line, filter):
    unicos = []
    izquierda = line[0].split(" ")
    for iz in izquierda:
        if len(iz) in filter:
            if iz not in unicos:
                unicos.append(iz)
    return sorted(unicos, key=len)

def findVariables(unicos, array960):
    a = [item for item in unicos[1] if item not in unicos[0]]
    eg = [item for item in unicos[3] if item not in unicos[0]
          and item not in unicos[1] and item not in unicos[2]]
    bd = [item for item in unicos[2] if item not in unicos[0]]
    cf = [item for item in unicos[2] if item in unicos[0]]
    cde = [item for item in array960[0] if item not in array960[1]]
    cde += [item for item in array960[1] if item not in array960[2]]
    cde += [item for item in array960[2] if item not in array960[0]]
    e = [item for item in eg if item in cde]
    g = [item for item in eg if item not in e]
    c = [item for item in cf if item in cde]
    f = [item for item in cf if item not in c]
    d = [item for item in bd if item in cde]
    b = [item for item in bd if item not in d]
    return a, b, c, d, e, f, g

def recorriendo():
    counter, array = 0, [[], [], [], [], [], [], [], [], [], []]
    for outputsLine in arrayOutputs:
        unicos = whichWith(outputsLine, [2, 3, 4, 7])
        array960 = whichWith(outputsLine, [6])
        a, b, c, d, e, f, g = findVariables(unicos, array960)

        array[0], array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9] = a+b+c+e+f+g, c+f, a+c+d+e+g, a+c+d+f+g, b+d+c+f, a+b+d+f+g, a+b+d+e+f+g, a+c+f ,a+b+c+d+e+f+g ,a+b+c+d+f+g

        stringNumber = ''
        derecha = outputsLine[1].strip().split(" ")
        for der in derecha:
            num = list(der)
            for i in range(10):
                if set(array[i]) == set(num):
                    stringNumber += str(i)
        counter += int(stringNumber)
    print(counter)

recorriendo()
