
# Parte 1
# montar sequencia de distancias crescentes
# inf 0 1 2 3 4 5 6 7 8 0 1 2

# Parte 2
# testo se é melhor comparar com o zero posterior
# ao invés do anterior

# min(output[i], (zero_pos - i))  

INF = -99
n = int(input())

fita = input().split()
zeros = [ ]
output = [ ]

# anotando aonde estão os zeros
for i in range( len(fita) ):
  if fita[i] == '0': zeros.append(i)

j = 0 # j percorre a sequencia de zeros
zero_pos = zeros[j] # zero_pos é a posição do próximo zero
valor = INF # o valor que a próxima posição deve assumir

# Parte 1
for i in range( len(fita) ):
  if i == zero_pos :
    j = (j+1) if (j + 1 != len(zeros)) else (j)
    zero_pos = zeros[j]
    valor = 0
  elif valor != INF :
    valor = valor + 1

  output.append(valor)

j = 0
zero_pos = zeros[j]

# Parte 2
for i in range( len(output) ):

  if i == zero_pos:
    if j + 1 == len(zeros): break
    j = j + 1
    zero_pos = zeros[j]
  elif output[i] == INF:
    output[i] = zero_pos - i
  else:
    output[i] = min(output[i], zero_pos - i)

texto_saida = ''

for i in range( len(output) ):
  if i == len(output) - 1:
    texto_saida = texto_saida + str(output[i])
  else:
    texto_saida = texto_saida + str(output[i]) + ' '

print(texto_saida)