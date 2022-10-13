
def maior(lista) :
  if len(lista) == 0 : return None
  maior = lista[0]

  for valor in lista:
    if valor > maior:
      maior = valor

  return maior

def menor(lista) :
  if len(lista) == 0 : return None
  menor = lista[0]

  for valor in lista:
    if valor < menor:
      menor = valor

  return menor

print( maior([1, 2, 3, 4, 7, 5, 6]) )
print( menor([3, 2, 1, 2, 3, 4, 7, 5, 6]) )