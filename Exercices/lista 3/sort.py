list = ["Ze", "Ana","Pedro", "Zulmira", "Aarao"]
#list = [25, 12, 6, 30,10,50,20] #funciona para números também

def achaMenor(lista, indiceProcurado=0):
    menor = lista[indiceProcurado]
    for i in range(indiceProcurado, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indiceProcurado = i
    return indiceProcurado

def selection_sort(lista): # selection sort
    for i in range(len(lista)):
        pos = achaMenor(lista, i)
        lista[i], lista[pos] = lista[pos], lista[i]
    return lista

def bubble_sort(lista):
  trocou = True
  while trocou == True:
    trocou = False

    for i in range(len(lista)-1):
      if lista[i] > lista[i+1]:
        lista[i], lista[i+1] = lista[i+1], lista[i]
        trocou = True

print (achaMenor(list, 3))
print(ordena(list))