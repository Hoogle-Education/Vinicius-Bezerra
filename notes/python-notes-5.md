# Funções

São procedimentos/subprogramas para que possamos manter o reuso e a flexibilidade durante o nossa código.

## Exemplo inicial (sem funções)

```py
nota_exatas1 = 9
nota_exatas2 = 6
nota_exatas3 = 8

nota_humanas1 = 9
nota_humanas2 = 6
nota_humanas3 = 8

print(f'Media = { (nota_exatas1*5 + nota_humanas1*2) / 7}')
```

## Exemplo com Funções

```py
def calcula_media(nota_exatas, nota_humanas):
  return (nota_exatas1*5 + nota_humanas1*2) / 7

def lorem():
  print('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum')

print(f'Media = {calcula_media(nota_exatas1, nota_humanas1)}')
lorem()
lorem()
lorem()
lorem()
```