n = int(input())

fita = input().split()
zeroMaisProximo = [ ]

for i in range(0, n, 0):

  if fita[i] == 0:
    zero_pos = i

    while i > 0:


   i = i + 1

# 13
# -1 0 -1 -1 -1 -1 -1 -1 -1 -1 0 -1 -1
# 1  
# 0  
# 1  
# 2  
# 3  
# min(output[i], (zero_pos - i))  
# (10 - 6)  
# (10 - 7)  
# (10 - 8)  
# (10 - 9) 
# 0