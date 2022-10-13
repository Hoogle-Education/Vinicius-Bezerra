
def ehPrimo(numero):
  for valor in range(2, numero):
    if numero % valor == 0 : 
      return False

  return True

def testaNumeros(limite):
  soma = 0
  for valor in range(2, limite+1):
    if ehPrimo(valor) :
      soma += valor
  print(soma)

testaNumeros(100)