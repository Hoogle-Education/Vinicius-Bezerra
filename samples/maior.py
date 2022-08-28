
n = int(input('digite a quantidade de entradas: '))

maior = None

for i in range( n ) :
  numero = int(input())

  if maior == None :
    maior = numero
  
  if numero > maior :
    maior = numero

print(f'O maior é {maior}')