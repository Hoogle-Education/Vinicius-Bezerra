tamanho = int(input())

sequencia = input().split()

contador = 0

for index in range( tamanho - 2 ) :

  verifica1  = (sequencia[index] == '1')
  verifica2 = (sequencia[index + 1] == '0')
  verifica3 = (sequencia[index + 2] == '0')

  if verifica1 and verifica2 and verifica3 :
    contador = contador + 1

print(contador)



