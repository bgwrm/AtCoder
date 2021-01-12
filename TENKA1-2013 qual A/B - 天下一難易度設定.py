n = int(input())
ans = 0
for i in range(n):
    x = [int(_) for _ in input().split()]
    if 0 <= sum(x) < 20:
        ans += 1
print(ans)