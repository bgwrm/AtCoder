n = int(input())
a = [int(_) for _ in input().split()]
c, ans = 1, 0
for i in range(n-1):
    if a[i] == a[i+1]:
        c += 1
    else:
        ans += c//2
        c = 1
ans += c//2
print(ans)