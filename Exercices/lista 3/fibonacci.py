
def iterativa(sequencia, n):
  for i in range(2, n+1):
    fibonacci.append(sequencia[i-1] + sequencia[i-2])

fibonacci = [0, 1]

iterativa(fibonacci, 10)

print(fibonacci)