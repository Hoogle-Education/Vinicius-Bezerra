# ---------------------------------
# variáveis globais

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