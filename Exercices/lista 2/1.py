
def ehPrimo(numero):
  for valor in range(2, numero):
    if numero % valor == 0 : 
      return False

  return True

def testaNumeros(limite):
  for valor in range(2, limite+1):
    if ehPrimo(valor) :
      print(valor, end=' ')


testaNumeros(200)