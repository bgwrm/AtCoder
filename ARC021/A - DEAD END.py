a = [[int(_) for _ in input().split()] for i in range(4)]
for i in range(4):
    for j in range(4):
        if i < 3 and a[i][j] == a[i+1][j]:
            print('CONTINUE')
            exit()
        if j < 3 and a[i][j] == a[i][j+1]:
            print('CONTINUE')
            exit()
print('GAMEOVER')