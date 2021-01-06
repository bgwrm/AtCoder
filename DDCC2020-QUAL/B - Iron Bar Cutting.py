import sys
n = int(input())
a = [int(_) for _ in input().split()]
total = sum(a)
ans, p = sys.maxsize, 0

for i in range(n-1):
    p += a[i]
    ans = min(ans, abs(total-2*p))

print(ans)