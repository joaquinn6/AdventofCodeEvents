maxCalories = list()
caloriesByElf = 0
with open("2022/dic01/input.txt","r") as archivo:
  for line in archivo:
    if line != '\n':
      caloriesByElf += int(line)
    else:
      if len(maxCalories) == 3:
        if caloriesByElf > maxCalories[0]:
          maxCalories.pop(0)
          maxCalories.append(caloriesByElf)
          maxCalories.sort()
      else: maxCalories.append(caloriesByElf)
      caloriesByElf = 0
print (sum(maxCalories))