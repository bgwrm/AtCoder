n, k = (int(_) for _ in input().split())
ans = 0

for i in range(1, n+1):
    dice = i
    count = 0
    while dice < k:
        dice *= 2
        count += 1
    ans += 1/(n * 2**count)

print(ans)