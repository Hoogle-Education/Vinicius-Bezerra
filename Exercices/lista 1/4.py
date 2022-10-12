# -------------------------------------------

from random import randint

# -------------------------------------------

naipes = ['paus', 'ouros', 'copas', 'espadas']
numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
baralho = [ ]

# -------------------------------------------

# retorna 1 se numero 1 for maior que numero 2
# retorna 0 se numero 1 for igual a numero 2
# retorna -1 se numero 1 for menor que numero 2
def comparaNumero(numero1, numero2) :

  if numero1 == numero2: return 0

  if numero1 == 'A' and numero2 != 'A': return -1
  if numero1 != 'A' and numero2 == 'A': return 1
  if numero1 == 'K' and numero2 != 'K': return 1
  if numero1 != 'K' and numero2 == 'K': return -1 

  if str(numero1).isnumeric() and not str(numero2).isnumeric(): return -1
  if not str(numero1).isnumeric() and str(numero2).isnumeric(): return 1

  if numero1 > numero2 : return 1

  return -1
  
# -------------------------------------------

def ordenaBaralho(baralho):

  for i in range(len(baralho)):
    menor = baralho[i]

    for j in range(i+1, len(baralho)):
      atual = baralho[j]

# -------------------------------------------

for i in range(0, 52):
  carta = {
    'naipe' : naipes[randint(0,3)],
    'numero' : numeros[randint(0, 12)]
  }

  baralho.append(carta)

for carta in baralho:
  print(f'Carta[ naipe: {carta["naipe"]} , numero : {carta["numero"]} ]')

baralho[0]['numero'] = 2
baralho[1]['numero'] = 'Q'

print(comparaNumero(baralho[0]['numero'], baralho[1]['numero']))