"""AoC dic 4 v2"""
import re
REGEX = r"(?=(XMAS|SAMX))"
lines = []
with open("2024/dic04/input.txt", "r", encoding='utf-8') as archivo:
  for line in archivo:
    lines.append(line.strip())
I_LENGTH = len(lines)
J_LENGTH = len(lines[0])

res = 0
for index_i, i in enumerate(lines):
  if index_i == 0 or index_i == I_LENGTH-1:
    continue
  for index_j, j in enumerate(i):
    if index_j == 0 or index_j == I_LENGTH-1:
      continue

    if j == 'A':
      if (lines[index_i-1][index_j-1] == 'M' and lines[index_i+1][index_j+1] == 'S') or lines[index_i-1][index_j-1] == 'S' and lines[index_i+1][index_j+1] == 'M':
        if (lines[index_i+1][index_j-1] == 'M' and lines[index_i-1][index_j+1] == 'S') or lines[index_i+1][index_j-1] == 'S' and lines[index_i-1][index_j+1] == 'M':
          res += 1

print(res)
