n, k = (int(_) for _ in input().split())
p = [int(_) for _ in input().split()]
ans = 0

p.sort()

for i in range(k):
    ans += p[i]

print(ans)