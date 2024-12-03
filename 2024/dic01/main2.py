"""AoC dic 1 v2"""
ids_left, ids_right = list([]), list([])
with open("2024/dic01/input.txt", "r") as archivo:
  for line in archivo:
    line_tuple = [int(x) for x in line.strip().split('   ')]
    ids_left.append(line_tuple[0])
    ids_right.append(line_tuple[1])

ids_left.sort()
ids_right.sort()
res = 0
for value in ids_left:
  res += value*(ids_right.count(value))
print(res)
