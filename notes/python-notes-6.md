# Dictionaries

Análogo a uma lista, porém ao invés de manipularmos posições sem nenhuma expressividade no código, manipulamos os dados através do par `[chave] = valor`

```py
lista = ['joao', 12, 1.75]
print(f'Nome: {lista[0]}, Idade: {lista[1]}, Altura: {lista[2]}m')
```

```py
pessoa = {
  'Nome': 'joao',
  'Idade': 12,
  'Altura': 1.75
}

print(f'Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Altura: {pessoa['Altura']}m')
```

## Como adicionar novos pares

```py
pessoa['Telefone'] = '(21) 2712-7230'
```

## Retornando todas as chaves

```py
print(pessoa.keys())
print(pessoa.values())
```

output
```
['Nome', 'Idade', 'Altura', 'Telefone']
['Joao', 12, 1.75, '(21) 2712-7230']
```

## Percorrendo todos os elementos um dicionario

```py
for key in pessoa.keys():
  print(f'{key} : {pessoa[key]}')
```