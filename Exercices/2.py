# ---------------------------------
# variáveis globais

from re import A


turma = [ ]
notas_acima = [ ]
notas_abaixo = [ ]

# ---------------------------------
# função que le entradas

def le_entadas(turma):
    nota = float(input('digite o nota: '))

    while nota >= 0 :
      nome = input('digite o nome deste aluno(a): ')
      
      aluno = {
        'nome' : nome,
        'nota' : nota
      }

      turma.append(aluno)

      nota = float(input('digite o nota: '))

# ---------------------------------

def calcula_media(turma):
  quantidade = float(len(turma))
  soma = 0.0
  
  for i in range( len(turma) ) :
    nota = turma[i]['nota']
    soma += nota
  
  return (soma / quantidade)

# ---------------------------------

def imprime_turma(turma):
  for i in range(len(turma)):
    print(f'Aluno: {turma[i]["nome"]} | Nota = {turma[i]["nota"]}')

# ---------------------------------

def distribui_notas(turma, notas_acima, notas_abaixo):
    media = calcula_media(turma)

    for i in range(len(turma)):
      aluno = turma[i]
      nota = aluno['nota']

      if nota >= media:
        notas_acima.append(aluno)
      else:
        notas_abaixo.append(aluno)

# ---------------------------------
# ordenando por nome

{}


def ordenaPorNota(turma):
  notas = [ ]

  for aluno in turma:
    notas.append(aluno['nota'])

  for i in range(len(turma)):
    # n [0 : i-1] : [i : final]
    pos_menor_nota = pos_menor(notas[i:]) + i

    aux = turma[i]
    turma[i] = turma[pos_menor_nota]
    turma[pos_menor_nota] = aux

    aux = notas[i]
    notas[i] = notas[pos_menor_nota]
    notas[pos_menor_nota] = aux

def ordenaPorNome(turma):
  nomes = [ ]

  for aluno in turma:
    nomes.append(aluno['nome'])

  for i in range(len(turma)):
    # n [0 : i-1] : [i : final]
    pos_menor_nome = pos_menor(nomes[i:]) + i

    aux = turma[i]
    turma[i] = turma[pos_menor_nome]
    turma[pos_menor_nome] = aux

    aux = nomes[i]
    nomes[i] = nomes[pos_menor_nome]
    nomes[pos_menor_nome] = aux
    
# ---------------------------------
# descobrindo posição do menor

def pos_menor(lista):
  indice_do_menor = None

  for i in range(len(lista)):

    elemento = lista[i]

    if indice_do_menor == None:
      indice_do_menor = i

    if elemento < lista[indice_do_menor]:
      indice_do_menor = i

  return indice_do_menor

# ---------------------------------
# aonde executa

le_entadas( turma )
# for elemento in turma:
#   print ( elemento )

print(f'media da turma = {calcula_media(turma)}')

print("### TODOS OS ALUNOS ###")
imprime_turma(turma)

distribui_notas(turma, notas_acima, notas_abaixo)

print("### NOTAS ACIMA ###")
imprime_turma(notas_acima)

print("### NOTAS ABAIXO ###")
imprime_turma(notas_abaixo)

print("### ORDENANDO POR NOTAS ###")
ordenaPorNota(turma)
imprime_turma(turma)


print("### ORDENANDO POR NOMES ###")
ordenaPorNome(turma)
imprime_turma(turma)