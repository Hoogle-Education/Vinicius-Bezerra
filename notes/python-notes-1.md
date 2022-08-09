# Entrada/Saída

```py
print('Hello world!')
```

## Variáveis

|tipo|ideia|
|:-:|:-:|
|`<int>`|inteiro|
|`<float>`|real|
|`<str>`|frases|
|`<bool>`|True ou False|

# Entradas

A função `input()` lê os dados sempre como `str` e também processa toda a linha de uma única vez.

```py
var = input()
```

nas entradas por vezes iremos forçar um tipo:

```py
nota = float( input() )
```

## Saídas formatadas

São feitas através do `print(f'...')`

servem para imprimir de maneira mais natural e possivelmente formatar a saída.

# Estruturas de seleção

## `if - elif - else`

```py
if nota >= 7.0 :
  print('ok')
else : 
  print('pode melhorar')
```

```py
if nota >= 9 :
  print('excelente!')

if nota < 9 and nota >= 7.0 :
  print('ok')
else:
  print('pode melhorar')
```

melhorando:

```py
nota = 9.5

if nota >= 9 :
  print('excelente!')
elif nota >= 7.0:
  print('ok')
else :
  print('pode melhorar')
```
