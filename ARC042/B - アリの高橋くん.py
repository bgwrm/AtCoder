def d(x0, y0, x1, y1, x2, y2):
    return abs((y2-y1)*x0-(x2-x1)*y0+x2*y1-y2*x1)/((x2-x1)**2+(y2-y1)**2)**0.5
x, y = (int(_) for _ in input().split())
n = int(input())
xy = [[int(_) for _ in input().split()] for i in range(n)]
print(min([d(x, y, xy[i-1][0], xy[i-1][1], xy[i][0], xy[i][1]) for i in range(n)]))