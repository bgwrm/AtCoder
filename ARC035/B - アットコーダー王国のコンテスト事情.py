from collections import Counter
import math
n = int(input())
t = sorted([int(input()) for _ in range(n)])
p, q = 0, 1
for i in range(n):
    p += t[i]*(n-i)
print(p)
for i in Counter(t).values():
    q *= math.factorial(i)
    q %= 10**9+7
print(q)