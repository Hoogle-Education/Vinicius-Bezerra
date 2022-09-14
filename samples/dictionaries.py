pessoa = {
  'Nome': 'joao',
  'Idade': 12,
  'Altura': 1.75
}

pessoa['Telefone'] = '(21) 2712-7230'

print('-----------------------')

print(pessoa.keys())
print(pessoa.values())

print('-----------------------')

for key in pessoa.keys():
  print(f'{key} : {pessoa[key]}')

print('-----------------------')