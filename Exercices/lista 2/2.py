def contains(array, target):
  for element in array:
    if element == target:
      return True

  return False

def ehVogal(char):
  vogais = ['a', 'e', 'i', 'o', 'u']
  if contains(vogais, char):
    return True

  return False

def isolaVogais(palavra):
  isola_vogais = ''
  for letra in palavra:
    if not ehVogal(letra):
      isola_vogais += letra
  
  return isola_vogais

print(isolaVogais('um teste de uma palavra em uma frase'))