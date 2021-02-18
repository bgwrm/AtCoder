n, c = (int(_) for _ in input().split())
a = [int(input()) for _ in range(n)]
e, o, m = [0]*10, [0]*10, 0
for i in range(n):
    if i%2: e[a[i]-1] += 1
    else: o[a[i]-1] += 1
for i in range(10):
    for j in range(10):
        if i != j:
            m = max(e[i]+o[j], m)
print(c*(n-m))