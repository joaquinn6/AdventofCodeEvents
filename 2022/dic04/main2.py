rangesOverlap = 0
with open("2022/dic04/input.txt","r") as archivo:
  for line in archivo:
    ranges = line.strip().split(',')
    sections = [(ranges[0].split('-')),(ranges[1].split('-'))]
    sections_ranges = [(list(range(int(sections[0][0]), int(sections[0][1])+1))), (list(range(int(sections[1][0]), int(sections[1][1])+1)))]
    lower_section = sections_ranges[0] if len(sections_ranges[0]) <= len(sections_ranges[1]) else sections_ranges[1]
    greater_section = sections_ranges[1] if len(sections_ranges[1]) >= len(sections_ranges[0]) else sections_ranges[0]
    for i in lower_section:
      if i in greater_section:
        rangesOverlap += 1
        break

print (rangesOverlap)