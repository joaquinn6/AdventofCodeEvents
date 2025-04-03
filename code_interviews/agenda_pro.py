"""NÚMEROS ROMANOS A ENTEROS:"""

numbers = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def to_int(numero_romano: str) -> int:
  letra_anterior = numero_romano[0]
  total = 0
  for letra in numero_romano:
    if numbers[letra_anterior] < numbers[letra]:
      total = total - numbers[letra_anterior]
      total = total + numbers[letra] - numbers[letra_anterior]
      letra_anterior = letra
      continue
    total += numbers[letra]
    letra_anterior = letra
  return total


print(to_int('MDCCCXXXVI'))


"""Validación de etiquetas de cierre"""


def is_valid(entrada: str) -> bool:
  characters = []
  for character in entrada:
    if character not in ['}', ']', ')']:
      characters.append(character)
      continue

    if len(characters) == 0:
      return False
    index_last = len(characters) - 1
    if character == '}':
      if characters[index_last] != '{':
        return False
    if character == ')':
      if characters[index_last] != '(':
        return False
    if character == ']':
      if characters[index_last] != '[':
        return False

    characters.pop(index_last)

  if len(characters) > 0:
    return False
  return True


print(is_valid('([][()])[]'))
