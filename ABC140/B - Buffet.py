n = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
c = [int(_) for _ in input().split()]
prev = -1
ans = 0

for i in range(n):
    ans += b[a[i]-1]
    if a[i] == prev + 1:
        ans += c[prev-1]
    prev = a[i]

print(ans)