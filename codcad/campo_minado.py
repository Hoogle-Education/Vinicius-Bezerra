n = int(input())
bombas = [ ]
output = [ ]

bombas.append(0) # criando bordas falsas

for i in range(n):
  bombas.append( int(input()) )

bombas.append(0) # criando bordas falsas

for i in range(1, n + 1) :
  output.append( bombas[i-1] + bombas[i] + bombas[i+1] )

for value in output :
  print(value)