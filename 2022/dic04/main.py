rangesOverlap = 0
with open("2022/dic04/input.txt","r") as archivo:
  for line in archivo:
    ranges = line.strip().split(',')
    sections = [(ranges[0].split('-')),(ranges[1].split('-'))]
    if int(sections[0][0]) <= int(sections[1][0]) and int(sections[0][1]) >= int(sections[1][1]):
      rangesOverlap+=1
    elif int(sections[1][0]) <= int(sections[0][0]) and int(sections[1][1]) >= int(sections[0][1]):
      rangesOverlap+=1
print (rangesOverlap)