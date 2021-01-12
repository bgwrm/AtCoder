n = int(input())
a, b = (int(_) for _ in input().split())
p = [int(_) for _ in input().split()]
p1, p2, p3 = 0, 0, 0
for i in range(n):
    if p[i] <= a:
        p1 += 1
    elif a < p[i] <= b:
        p2 += 1
    elif b < p[i]:
        p3 += 1
print(min(p1, p2, p3))