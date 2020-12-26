k, s = (int(_) for _ in input().split())
ans = 0
for i in range(k+1):
    for j in range(k+1):
        if i + j + k >= s and i + j <= s:
            ans += 1
print(ans)