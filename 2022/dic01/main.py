maxCalories = 0
caloriesByElf = 0
with open("2022/dic01/input.txt","r") as archivo:
  for line in archivo:
    if line != '\n':
      caloriesByElf += int(line)
    else:
      if caloriesByElf > maxCalories:
        maxCalories = caloriesByElf
      caloriesByElf = 0
print (maxCalories)