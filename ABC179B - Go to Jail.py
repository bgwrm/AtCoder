n = int(input())
d = [[int(_) for _ in input().split()] for i in range(n)]

for i in range(n - 2):
    if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
        print('Yes')
        exit()

print('No')