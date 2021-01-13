import math
n = int(input())
i = int(math.sqrt(n*2))
while n+1 >= i*(i+1)//2:
    i += 1
print(n-i+2)