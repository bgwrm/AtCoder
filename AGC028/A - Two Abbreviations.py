import math
n, m = (int(_) for _ in input().split())
s = input()
t = input()
g = math.gcd(n,m)
l = (n*m)//g
for i in range(g):
    if s[i*n//g] != t[i*m//g]:
        print(-1)
        exit()
print(l)