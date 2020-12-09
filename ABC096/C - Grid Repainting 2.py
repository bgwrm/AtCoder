h, w = (int(_) for _ in input().split())
s = [input() for i in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            flg = False
            if i != 0:
                if s[i - 1][j] == "#":
                    flg = True
            if i != h - 1:
                if s[i + 1][j] == "#":
                    flg = True
            if j != 0:
                if s[i][j - 1] == "#":
                    flg = True
            if j != w - 1:
                if s[i][j + 1] == "#":
                    flg = True
            if flg == False:
                print("No")
                exit()

print("Yes")