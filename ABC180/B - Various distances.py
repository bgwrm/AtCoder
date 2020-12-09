import math

n = int(input())
x = [int(_) for _ in input().split()]
md = 0
ed = 0
cd = 0

for i in range(n):
    md += abs(x[i])
    ed += abs(x[i]) ** 2
    if abs(x[i]) > cd:
        cd = abs(x[i])

print(md)
print(math.sqrt(ed))
print(cd)