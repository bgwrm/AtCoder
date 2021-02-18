n, k = (int(_) for _ in input().split())
c1 = c2 = 0
for i in range(1, n+1):
    if i%k == 0:
        c1 += 1
    elif k%2 == 0 and i%k == k//2:
        c2 += 1
print(c1**3+c2**3)