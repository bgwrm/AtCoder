n, t = (int(_) for _ in input().split())
l = [int(_) for _ in input().split()]
w = 0
for i in range(1, n):
    w += max(l[i-1] + t - l[i], 0)
print(n * t - w)