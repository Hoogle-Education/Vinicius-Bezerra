linha = input().split()

p1 = int(linha[0])
c1 = int(linha[1])
p2 = int(linha[2])
c2 = int(linha[3])

produto1 = p1*c1
produto2 = p2*c2

if produto1 == produto2:
  print("0")
elif produto1 > produto2:
  print("-1")
else:
  print("1")