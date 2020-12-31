import math
n = int(input())
r = sorted([int(input()) for _ in range(n)])
a1, a2 = 0, 0
for i in range(0,n,2):
    a1 += r[i]**2
for i in range(1,n,2):
    a2 += r[i]**2
print(abs(a1-a2)*math.pi)