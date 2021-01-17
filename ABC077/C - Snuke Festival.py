import bisect
n = int(input())
a = sorted([int(_) for _ in input().split()])
b = sorted([int(_) for _ in input().split()])
c = sorted([int(_) for _ in input().split()])
ans = 0
for i in b:
    ans += bisect.bisect_left(a,i)*(n-bisect.bisect_right(c,i))
print(ans)