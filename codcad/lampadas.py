# configurando as lampadas para apagadas
lampA = 0
lampB = 0

quantidadeInterruptor1 = 0
quantidadeInterruptor2 = 0

# inserindo quantidade de entradas
n = int(input('digite a quantidade de operações: '))

# inserindo as operacoes com as lampadas
operacoes = input('digite a lista: ').split()

for index in range(n):
  operacoes[index] = int(operacoes[index])

  if operacoes[index] == 1:
    quantidadeInterruptor1 = quantidadeInterruptor1 + 1
  else:
    quantidadeInterruptor2 = quantidadeInterruptor2 + 1

if (quantidadeInterruptor2 % 2 == 1) :
  lampB = 1

total = quantidadeInterruptor1 + quantidadeInterruptor2

if (total%2 == 1) :
  lampA = 1

print(lampA)
print(lampB)