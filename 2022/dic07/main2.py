lines = list()
with open("2022/dic07/input.txt","r") as archivo:
  for line in archivo:
    lines.append(line.strip().split(' '))

directories = dict()
directories_list = list()
cursor = []
total_size = []

def comando(line):
  if line[1] == 'cd':
    if line[2] == '..':
      cursor.pop()
    else:
      cursor.append(line[2])
      check_dir()

def check_dir():
  directories['/'.join(cursor)] = 0
  directories_list.append('/'.join(cursor))

def file_count(line):
  size = int(line[0])
  total_size.append(size)
  cursor_copy = list(cursor)
  for _ in cursor:
    directories['/'.join(cursor_copy)] += size
    cursor_copy.pop()


for line in lines:
  if line[0] == "$":
    comando(line)
  elif line[0] != 'dir':
    file_count(line)

sizes = list()
for directory in directories_list:
  sizes.append(directories[directory])

sizes.sort()
space_free = 70000000 - sum(total_size)
space_need = 30000000 - space_free

for size in sizes:
  if size > space_need:
    print (size)
    break