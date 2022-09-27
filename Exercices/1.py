# ----------------------------

def eh_primo(numero):

  for valor in range(2, numero):
    if numero % valor == 0 :
      return False
    
  return True

# ----------------------------

n = int(input('digite um numero: '))

for i in range(2, n+1):
  if eh_primo(i) :
    print(i , end=' ')

# ----------------------------