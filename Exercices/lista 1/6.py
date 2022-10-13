# ---------------------------

def leitura():
  entradas = [ ]
  numero = int(input())

  while numero >= 0 :
    entradas.append(numero)
    numero = int(input())

  return entradas

# ---------------------------

def maior(lista):
  maior = lista[0]

  for valor in lista:
    if valor > maior : maior = valor
  
  return maior

# ---------------------------

def quantidade(lista):
  return len(lista)

# ---------------------------

def media(lista):
  tamanho = quantidade(lista)
  soma = 0

  for valor in lista: soma += valor

  return (soma / tamanho)

# ---------------------------

lista = leitura()
print(f'maior = {maior(lista)}')
print(f'quantidade = {quantidade(lista)}')
print(f'media = {media(lista)}')