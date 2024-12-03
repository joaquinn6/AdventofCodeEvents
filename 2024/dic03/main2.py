"""AoC dic 3 v2"""
import re

REGEX = r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))"
data = ""
with open("2024/dic03/input.txt", "r", encoding='utf-8') as archivo:
  data = archivo.read()


def _do_mul(mul_item: str) -> int:
  mul_item = str(mul_item).replace('mul', '').replace(
      '(', '').replace(')', '').split(',')
  return int(mul_item[0]) * int(mul_item[1])


data = re.findall(REGEX, data)
is_enable = True
res = 0
for item in data:
  if "don't()" == item:
    is_enable = False

  if "do()" == item:
    is_enable = True

  if "mul" in item and is_enable:
    res += _do_mul(item)
print(res)
