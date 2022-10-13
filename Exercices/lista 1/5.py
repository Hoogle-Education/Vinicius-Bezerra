
def leituraMatrix():
  linhas = int(input('quantidade linhas: '))
  colunas = int(input('quantidade colunas: '))
  matrix = [ ]

  for i in range(linhas):
    leitura = input().split()
    linha_matrix = [ ]
    for j in range(colunas):
      linha_matrix.append(int(leitura[j]))
    
    matrix.append(linha_matrix)
  
  return matrix

def trocaDiagonalSecundaria(matrix):
  tamanho = len(matrix)
  for i in range(tamanho):
    matrix[i][tamanho-i-1] = 1

def printMatrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(matrix[i][j], end=' ')
    print()


mat = leituraMatrix()
trocaDiagonalSecundaria(mat)
printMatrix(mat)

# [0][0] [0][1] [0][2]
# [1][0] [1][1] [1][2]
# [2][0] [2][1] [2][2]

# [i][?]

# i + ? = n-1
# ? = n-i-1

# diag principal = matrix[i][i]
# diag sec = matrix[i][n-i-1]