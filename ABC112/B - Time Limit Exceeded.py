n, t = (int(_) for _ in input().split())
ct = sorted([[int(_) for _ in input().split()] for i in range(n)])

for i in ct:
    if i[1] <= t:
        print(i[0])
        exit()
print('TLE')