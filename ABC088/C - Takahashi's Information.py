c = [[int(_) for _ in input().split()] for i in range(3)]

for i in range(2):
    if c[1][0] - c[0][0] != c[1][i+1] - c[0][i+1] or c[2][0] - c[0][0] != c[2][i+1] - c[0][i+1] or c[0][1] - c[0][0] != c[i+1][1] - c[i+1][0] or c[0][2] - c[0][0] != c[i+1][2] - c[i+1][0]:
        print('No')
        exit()

print('Yes')