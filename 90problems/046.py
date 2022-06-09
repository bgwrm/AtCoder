from collections import Counter
n = int(input())
a = Counter([int(_)%46 for _ in input().split()])
b = Counter([int(_)%46 for _ in input().split()])
c = Counter([int(_)%46 for _ in input().split()])
ans = 0
for i in range(46):
    ca = a[i]
    for j in range(46):
        ans += ca*b[j]*c[(46-i-j)%46]
print(ans)