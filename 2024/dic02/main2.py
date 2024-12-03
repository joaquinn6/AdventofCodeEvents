"""AoC dic 2 v2"""
lines = list([])
with open("2024/dic02/input.txt", "r", encoding='utf-8') as archivo:
  for line in archivo:
    lines.append([int(x.strip()) for x in line.split(' ')])


def _is_valid_report(report: list) -> bool:

  sort = ''
  for i in range(1, len(report)):
    dif = report[i-1] - report[i]
    if dif > 3 or dif < -3 or dif == 0:
      return False

    if sort == '':
      sort = 'ascending' if dif > 0 else 'descending'
    else:
      if sort == 'ascending' and dif < 0:
        return False

      if sort == 'descending' and dif > 0:
        return False

  return True


def _is_valid_without_one_level(report: list) -> bool:
  if _is_valid_report(report):
    return True

  for i in range(0, len(report)):
    report_without_index = [level for j, level in enumerate(report) if j != i]
    if _is_valid_report(report_without_index):
      return True
  return False


res = 0
for line in lines:
  res += 1 if _is_valid_without_one_level(line) else 0

print(res)
