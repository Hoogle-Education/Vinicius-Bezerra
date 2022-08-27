#  -------------------------------------

# criando uma lista
colors = ['red', 'green', 'blue']
greyscale = ['white', 'grey', 'black']

# adicionando elemento no final
colors.append('yellow')

# insere em uma posição e já reajusta a lista
colors.insert(2, 'purple')

# insere uma lista ao final da lista
colors.extend( greyscale )

# remove o ultimo elemnto
colors.pop()

# Ordeno a lista (neste caso, ordem alfabetica)
colors.sort()

# procuro o indice de um determinado elemento
bluePosition = colors.index('blue') + 1

#  -------------------------------------

print(f'TYPE = {type(colors)}')

print(f'position of "blue" : {bluePosition}')

# printando um elemento
print(colors[1])

# printando todos os elementos
print(colors)

#  -------------------------------------