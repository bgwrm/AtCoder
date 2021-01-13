a, k = (int(_) for _ in input().split())
d = 0
if k == 0:
    print(2*10**12-a)
    exit()
while a < 2*10**12:
    a += a*k+1
    d += 1
print(d)