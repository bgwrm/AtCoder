n = int(input())
p = [int(_) for _ in input().split()]
ans = 0

for i in range(n-2):
    if sorted(p[i:i+3])[1] == p[i+1]:
        ans += 1

print(ans)