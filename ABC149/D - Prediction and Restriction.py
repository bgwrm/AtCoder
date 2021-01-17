n, k = (int(_) for _ in input().split())
r, s, p = (int(_) for _ in input().split())
t = list(input())
for i in range(n-k):
    if t[i] == t[i+k]:
        t[i+k] = '0'
print(p*t.count('r')+r*t.count('s')+s*t.count('p'))