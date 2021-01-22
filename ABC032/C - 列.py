n, k = (int(_) for _ in input().split())
s = [int(input()) for _ in range(n)]
ans, j, p = 0, 0, 1
for i in range(n):
    p *= s[i]
    if p == 0:
        ans = n
        break
    elif p <= k:
        ans = max(i-j+1, ans)
    else:
        p //= s[j]
        j += 1
print(ans)