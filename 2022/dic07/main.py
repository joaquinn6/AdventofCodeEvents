lines = list()
with open("2022/dic07/input.txt","r") as archivo:
  for line in archivo:
    lines.append(line.strip().split(' '))

directories = dict()
directories_list = list()
cursor = []

def comando(line):
  if line[1] == 'cd':
    if line[2] == '..':
      cursor.pop()
    else:
      cursor.append(line[2])
      checkDir()

def checkDir():
  directories['/'.join(cursor)] = 0
  directories_list.append('/'.join(cursor))

def fileCount(line):
  size = int(line[0])
  cursorCopy = list(cursor)
  for _ in cursor:
    directories['/'.join(cursorCopy)] += size
    cursorCopy.pop()

for line in lines:
  if line[0] == "$":
    comando(line)
  elif line[0] != 'dir':
    fileCount(line)

sizes = list()
for directory in directories_list:
  if directories[directory] <= 100000:
    sizes.append(directories[directory])

print (sum(sizes))