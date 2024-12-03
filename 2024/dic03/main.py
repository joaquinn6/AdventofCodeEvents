"""AoC dic 3"""
import re

REGEX = 'mul\(\d{1,3},\d{1,3}\)'
data = ""
with open("2024/dic03/input.txt", "r", encoding='utf-8') as archivo:
  data = archivo.read()

data = [str(item).replace('mul', '').replace('(', '').replace(')',
                                                              '').split(',') for item in re.findall(REGEX, data)]

res = 0
for item in data:
  res += int(item[0]) * int(item[1])
print(res)
