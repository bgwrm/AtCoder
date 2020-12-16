a = [[int(_) for _ in input().split()] for i in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
for i in range(3):
    for j in range(3):
        if a[i][j] in b:
            a[i][j] = 1000

for i in range(3):
    if (a[i][0] == 1000 and a[i][1] == 1000 and a[i][2] == 1000) or (a[0][i] == 1000 and a[1][i] == 1000 and a[2][i] == 1000):
        print('Yes')
        exit()

if (a[0][0] == 1000 and a[1][1] == 1000 and a[2][2] == 1000) or (a[0][2] == 1000 and a[1][1] == 1000 and a[2][0] == 1000):
    print('Yes')
    exit()

print('No')