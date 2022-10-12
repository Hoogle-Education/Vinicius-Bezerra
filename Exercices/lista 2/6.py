def divisores(numero):
  divisores = [ ]
  for i in range(1, numero):
    if numero%i == 0:
      divisores.append(i)
  
  return divisores

def somaVetor(vetor):
  soma = 0
  for valor in vetor :
    soma += valor
  return soma

def ehNumeroPerfeito(numero):
  return numero == somaVetor(divisores(numero))

def encontraOs4PrimeirosPerfeitos():
  quantidade = 1
  numero = 1
  
  while quantidade <= 4 :
    if ehNumeroPerfeito(numero) :
      quantidade += 1
      print(numero)

    numero += 1

encontraOs4PrimeirosPerfeitos()

