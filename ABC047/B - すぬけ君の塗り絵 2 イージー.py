w, h, n = (int(_) for _ in input().split())
xya = [[int(_) for _ in input().split()] for i in range(n)]
p1, p2 = [0,0], [w,h]

for i in xya:
    if i[2] == 1:
        p1[0] = max(p1[0], i[0])
    elif i[2] == 2:
        p2[0] = min(p2[0], i[0])
    elif i[2] == 3:
        p1[1] = max(p1[1], i[1])
    else:
        p2[1] = min(p2[1], i[1])

print(max(p2[0]-p1[0],0)*max(p2[1]-p1[1],0))