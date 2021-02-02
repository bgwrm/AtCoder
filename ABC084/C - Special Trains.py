n = int(input())
csf = [[int(_) for _ in input().split()] for i in range(n-1)]
for i in range(n):
    t = 0
    for c, s, f in csf[i:]:
        if t < s:
            t = s
        elif t%f != 0:
            t += f-t%f
        t += c
    print(t)