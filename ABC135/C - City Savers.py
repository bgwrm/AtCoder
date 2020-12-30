n = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
ans = 0

for i in range(n):
    if a[i] >= b[i]:
        ans += b[i]
    else:
        ans += a[i]
        if b[i] - a[i] > a[i+1]:
            ans += a[i+1]
            a[i+1] = 0
        else:
            ans += b[i] - a[i]
            a[i+1] = a[i+1] - b[i] + a[i]

print(ans)