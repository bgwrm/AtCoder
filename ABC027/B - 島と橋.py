n = int(input())
a = [int(_) for _ in input().split()]
avg = sum(a)/n
l = []
ans = 0

if not float.is_integer(avg):
    print(-1)
    exit()

for i in range(n):
    l += [a[i]]
    if sum(l)/len(l) == avg:
        l = []
    else:
        ans += 1
print(ans)