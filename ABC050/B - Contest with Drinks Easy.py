n = int(input())
t = [int(_) for _ in input().split()]
m = int(input())
px = [[int(_) for _ in input().split()] for i in range(m)]
nodrink = sum(t)

for i in px:
    print(nodrink + i[1] - t[i[0]-1])