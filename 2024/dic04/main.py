"""AoC dic 4"""
import re
REGEX = r"(?=(XMAS|SAMX))"
lines = []
with open("2024/dic04/input.txt", "r", encoding='utf-8') as archivo:
  for line in archivo:
    lines.append(line.strip())
I_LENGTH = len(lines)
J_LENGTH = len(lines[0])

lines_inverse = [line[::-1] for line in lines]


def _is_valid_next_index(i_i: int, i_j: int) -> bool | tuple:
  if i_i + 1 >= I_LENGTH:
    return False

  if i_j + 1 >= J_LENGTH:
    return False

  return True


def _get_diagonal_line(first_letter, i_i: int, i_j: int, inverse: bool) -> str:
  diagonal_line = first_letter
  while _is_valid_next_index(i_i, i_j):
    i_i, i_j = i_i + 1, i_j + 1
    if inverse:
      diagonal_line += lines_inverse[i_i][i_j]
    else:
      diagonal_line += lines[i_i][i_j]
  return diagonal_line


def _get_vertical_line(first_letter, i_i: int, i_j: int) -> str:
  vertical_line = first_letter
  while i_i + 1 < I_LENGTH:
    i_i += 1
    vertical_line += lines[i_i][i_j]
  return vertical_line


lines_text = lines[:]
for index_i, i in enumerate(lines):
  for index_j, j in enumerate(i):
    if index_i == 0:
      lines_text.append(_get_vertical_line(j, index_i, index_j))
      lines_text.append(_get_diagonal_line(j, index_i, index_j, False))
      lines_text.append(_get_diagonal_line(
          lines_inverse[index_i][index_j], index_i, index_j, True))

    if index_j == 0 and index_i != 0:
      lines_text.append(_get_diagonal_line(j, index_i, index_j, False))
      lines_text.append(_get_diagonal_line(
          lines_inverse[index_i][index_j], index_i, index_j, True))

res = 0
for line in lines_text:
  res += len(re.findall(REGEX, line))
print(res)
