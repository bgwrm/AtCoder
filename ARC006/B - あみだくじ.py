n, l = (int(_) for _ in input().split())
o = [_ for _ in range(1, n+1)]
for _ in range(l):
    a = input()
    for i in range(1, 2*n-1, 2):
        if a[i] == '-':
            p, q = o[i//2], o[i//2+1]
            o[i//2] = q
            o[i//2+1] = p
print(o[(input().index('o'))//2])