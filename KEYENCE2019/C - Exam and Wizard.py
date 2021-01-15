n = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
c = p = ans = 0
l = []
if sum(a) < sum(b):
    print(-1)
    exit()
for i in range(n):
    if a[i] < b[i]:
        p += b[i]-a[i]
        ans += 1
    else:
        l += [a[i]-b[i]]
l = sorted(l, reverse=True)
while p > 0:
    p -= l[c]
    c += 1
    ans += 1
print(ans)