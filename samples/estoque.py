# inicialização
estoque = int(input('digite o estoque atual: '))

while estoque != 0 : # verificação
  if estoque > 0 :
    print(f'estou vendendo! sobrando = {estoque}')
    estoque = estoque - 1 # atualização
  else :
    print(f'estou comprando! faltando = {abs(estoque)}')
    estoque = estoque + 1 # atualização

print('loja fechou')