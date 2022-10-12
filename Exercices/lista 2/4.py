def contemNoVetor(array, target):
  for element in array:
    if element == target:
      return True

def converteAcentos(alvo):
  acentuacoes = {
    'a' : ['á', 'à', 'ã', 'â'],
    'e' : ['é', 'ê'],
    'o' : ['ó', 'õ'],
    'i' : ['í'],
    'u' : ['ú']
  }

  for chave in acentuacoes.keys():
    if contemNoVetor(acentuacoes[chave], alvo):
      return chave

  return str(alvo)

def removeAcentos(texto):
  copy = texto
  texto = ''
  for i in range(len(copy)):
    texto += converteAcentos(copy[i])

  return texto

print(removeAcentos('hoje é dia de acão de gracàs'))