import informe
import re
class reto3:
  def main(self):
    strOx, j= '', 0
    informeListOx= informe.informe()
    for j in range(12):
      ceros, unos = 0, 0
      if len(informeListOx) > 1:
        for info in informeListOx:
          if info!='':
            splitted = list(info)
            if splitted[j]=='1':
              unos +=1
            else:
              ceros+=1
        if unos > ceros:
          strOx += '1'
        elif unos < ceros:
          strOx += '0'
        else:
          strOx += '1'
        r = re.compile(strOx +".*")
        informeListOx = list(filter(r.match, informeListOx))
      else:
        strOx += list(informeListOx[0])[j]

    strCo, j= '', 0
    informeListCo= informe.informe()
    for j in range(12):
      ceros, unos = 0, 0
      if len(informeListCo) > 1:        
        for info in informeListCo:
          if info!='':
            splitted = list(info)
            if splitted[j]=='1':
              unos +=1
            else:
              ceros+=1
        if unos > ceros:
          strCo += '0'
        elif unos < ceros:
          strCo += '1'
        else:
          strCo += '0'
        r = re.compile(strCo +".*")
        informeListCo = list(filter(r.match, informeListCo))
      else:
        strCo += list(informeListCo[0])[j]
    print('result=>' + str(int(str(''.join(map(str, strCo))), 2) * int(str(''.join(map(str, strOx))), 2)))
reto=reto3()
reto.main()