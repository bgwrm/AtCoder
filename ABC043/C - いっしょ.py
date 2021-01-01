n = int(input())
a = [int(_) for _ in input().split()]
ans = 10**9

for i in range(min(a), max(a)+1):
    c = 0
    for j in a:
        c += (j-i)**2
    ans = min(ans, c)

print(ans)