n = int(input())
k = [int(_) for _ in input().split()]
ans = [k[0]]
for i in range(1,n-1):
    ans += [min(k[i], k[i-1])]
ans += [k[-1]]
print(*ans)