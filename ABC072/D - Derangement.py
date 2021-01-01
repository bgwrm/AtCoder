n = int(input())
p = [int(_) for _ in input().split()]
ans = 0

for i in range(n-1):
    if p[i] == i+1:
        n1 = p[i]
        n2 = p[i+1]
        p[i] = n2
        p[i+1] = n1
        ans += 1
if p[-1] == n:
    ans += 1

print(ans)