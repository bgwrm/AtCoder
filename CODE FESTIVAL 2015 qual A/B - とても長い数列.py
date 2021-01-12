n = int(input())
a = [int(_) for _ in input().split()]
ans = 0
for i in range(n):
    ans += ans + a[i]
print(ans)