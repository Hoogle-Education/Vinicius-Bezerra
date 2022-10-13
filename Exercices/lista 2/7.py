# ----------------------------------------

def verificaDimensoes(matrix1, matrix2):
  if len(matrix1) != len(matrix2): return False
  if len(matrix1[0]) != len(matrix2[0]): return False
  return True

# ----------------------------------------

def verificaDimensoesProduto(matrix1, matrix2):
  if len(matrix1[0]) != len(matrix2): return False
  return True

# ----------------------------------------

def verificaQuadrada(matrix):
  if len(matrix[0]) != len(matrix): return False
  return True

# ----------------------------------------

def somaMatrix(matrix1, matrix2):
  linhas = None
  colunas = None
  resultado = [ ]

  if verificaDimensoes(matrix1, matrix2):
      linhas = len(matrix1)
      colunas = len(matrix1[0])
  else: 
    return None

  for i in range(linhas):
    linha_resultado = []
    for j in range(colunas):
      linha_resultado.append(matrix1[i][j] + matrix2[i][j])
    resultado.append(linha_resultado)

  return resultado

# ----------------------------------------

def subtraiMatrix(matrix1, matrix2):
  linhas = None
  colunas = None
  resultado = [ ]

  if verificaDimensoes(matrix1, matrix2):
      linhas = len(matrix1)
      colunas = len(matrix1[0])
  else: 
    return None

  for i in range(linhas):
    linha_resultado = []
    for j in range(colunas):
      linha_resultado.append(matrix1[i][j] - matrix2[i][j])
    resultado.append(linha_resultado)

  return resultado

# ----------------------------------------

def produtoLinhaColuna(vlinha, vcoluna):
  resultado = 0
  for i in range(len(vlinha)):
    resultado += (vlinha[i]*vcoluna[i])

  return resultado

# ----------------------------------------

def extraiColuna(index, matrix):
  column = [ ]
  for k in range(len(matrix)):
    column.append(matrix[k][index])

  return column

# ----------------------------------------

def multiplicaMatriz(matrix1, matrix2):

  if not verificaDimensoesProduto(matrix1, matrix2):
    return None

  linhas = len(matrix1)
  colunas = len(matrix2[0])

  resultado = [ ]

  for i in range(linhas):
    linha = [ ]
    for j in range(colunas):
      vlinha = matrix1[i]
      vcoluna = extraiColuna(j, matrix2)
      linha.append(produtoLinhaColuna(vlinha, vcoluna))
    resultado.append(linha)
  
  return resultado

# ----------------------------------------

def determinante(matrix):

  if not verificaQuadrada:
    print('não é possível calcular este determinante')
  
  if len(matrix) > 3:
    print('tamanho de det não suportado')
  
  if len(matrix) == 1:
    return matrix[0][0]

  if len(matrix) == 2:
    return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
  
  if len(matrix) == 3:
    op1 = matrix[0][0]*matrix[1][1]*matrix[2][2]
    op2 = matrix[0][1]*matrix[1][2]*matrix[2][0]
    op3 = matrix[0][2]*matrix[1][0]*matrix[2][1]
    op4 = matrix[0][2]*matrix[1][1]*matrix[2][0]
    op5 = matrix[0][1]*matrix[1][0]*matrix[2][2]
    op6 = matrix[0][0]*matrix[1][2]*matrix[2][1]
    return op1 + op2 + op3 - op4 - op5 - op6


# ----------------------------------------

def printMatrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      print(matrix[i][j], end=' ')
    print()

# ----------------------------------------


array2d_1 = [ [1,	2, 3,	4],
	        [5,	5, 6,	6],
	        [-1, -2, -3, -4]
        ]

array2d_2 = [
          [1, 2, 3, -2, -3],
          [-4, -5, 6, 7, 1],
          [2, -3, 4, -5, 6],
          [7, 8, -1, -1, 2]
        ]

matrix_teste1 = [ [6, 1, 2], [1, 1, 3], [2, 2, 4]]
matrix_teste2 = [ [1, 1, 1], [1, 1, 1], [2, 2, 2]]

# TESTANDO MULTIPLICAÇÃO

teste = multiplicaMatriz(array2d_1, array2d_2)

printMatrix(teste)
print('-----------------------------')

# TESTANDO SOMA
printMatrix(somaMatrix(matrix_teste1, matrix_teste2))
print('-----------------------------')

# TESTANDO SUBTRAÇÃO
printMatrix(subtraiMatrix(matrix_teste1, matrix_teste2))
print('-----------------------------')

printMatrix(matrix_teste1)
print(f'determinante = {determinante(matrix_teste1)}')
