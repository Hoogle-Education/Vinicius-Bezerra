
def atualiza_matriz(matriz):
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j] = (i+1)*(j+1) - 3*(j+1)

  return matriz

matriz = [ [1, 2, 3],
           [3, 4, 5],
           [5, 6, 7] ]

atualiza_matriz(matriz)
print(matriz)