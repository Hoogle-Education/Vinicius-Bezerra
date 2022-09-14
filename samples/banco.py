
#dicionario
contaDoJoao = {
  'Pessoa': {
    'Nome': 'João',
    'Idade': 25
  },
  'Saldo': 0.0
}

#operações em cima do dicionário
def depositar(conta, quantia):
  conta['Saldo'] += quantia

def sacar(conta, quantia):
  saldo = conta['Saldo']

  if saldo > quantia:
    conta['Saldo'] -= quantia


# stack: estático
# heap: dinâmico

print(contaDoJoao['Pessoa']['Nome'])
depositar(contaDoJoao, 200)
depositar(contaDoJoao, 200)
depositar(contaDoJoao, 200)
sacar(contaDoJoao, 225)

print(f'Nome: {contaDoJoao["Pessoa"]}, Saldo = R${contaDoJoao["Saldo"]:.2f}')
