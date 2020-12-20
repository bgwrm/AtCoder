h, w = (int(_) for _ in input().split())
a = [[int(_) for _ in input().split()] for i in range(h)]
min = 100
total = 0

for i in range(h):
    for j in range(w):
        total += a[i][j]
        if a[i][j] < min:
            min = a[i][j]

print(total-h*w*min)