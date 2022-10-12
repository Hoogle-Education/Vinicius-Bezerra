def espalhaP(texto):
  palavras = texto.split()
  texto = ''

  for i in range(len(palavras)):
    palavra = palavras[i]
    texto += 'P' + palavra + ' '

  return texto.rstrip()

print( espalhaP('um texto para espalhar a letra') )
  