import bisect
n, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
ans, d, t = 0, [0], 0
for i in a:
    t += i
    d += [t]
for i in range(n):
    ans += n-bisect.bisect_left(d, d[i]+k)+1
print(ans)