def criaMatriz(linhas,colunas,valor = 0):
    #mat = ['inicializa com qualquer coisa que não seja vazia'] * linhas
    mat = ['blz'] * linhas
    print(mat)
    for lin in range(linhas):
        mat[lin] = [valor] * colunas #substitui a coisa pelos zeros
    
    print(mat)
    return mat

print("-------------- matriz")
#mat = criaMatriz(3,4)

def inicializarMatriz(linhas, colunas, formula):
    mat = criaMatriz(linhas, colunas)
    # usar a lei de formação Mij = ij - 3j
    for lin in range(linhas):
        for col in range(colunas):
            i = lin + 1 #adaptando Python para enunciado do ENEM
            j = col + 1
            # atenção para o que será pedido em avaliação
            texto = formula
            mat[lin][col] = eval(texto) # estudem eval !
    return mat

mat = inicializarMatriz(2, 2, "i*j - 3*j")
for i in range (len(mat)):
    print(mat[i])