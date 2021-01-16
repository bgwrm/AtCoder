n = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
ma, mb, mab = a[0], b[0], a[0]*b[0]
for i in range(n):
    if a[i] > ma:
        ma = a[i]
        mb = b[i]
    else:
        mb = max(b[i], mb)
    mab = max(ma*mb, mab)
    print(mab)