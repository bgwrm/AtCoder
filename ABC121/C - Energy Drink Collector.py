n, m = (int(_) for _ in input().split())
ab = sorted([[int(_) for _ in input().split()] for i in range(n)])
i, ans = 0, 0

while True:
    if m > 0 and ab[i][1] > 0:
        ans += ab[i][0]
        ab[i][1] -= 1
        m -= 1
    if m == 0:
        break
    if ab[i][1] == 0:
        i += 1

print(ans)