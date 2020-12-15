h, w = (int(_) for _ in input().split())
s = [input() for i in range(h)]
ans = [[0]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = -5000
            if i != 0:
                ans[i-1][j] += 1
                if j != 0:
                    ans[i-1][j-1] += 1
                if j != w-1:
                    ans[i-1][j+1] += 1
            if i != h-1:
                ans[i+1][j] += 1
                if j != 0:
                    ans[i+1][j-1] += 1
                if j != w-1:
                    ans[i+1][j+1] += 1
            if j != 0:
                ans[i][j-1] += 1
            if j != w-1:
                ans[i][j+1] += 1

for i in range(h):
    for j in range(w):
        if ans[i][j] < 0:
            ans[i][j] = -1
    print(''.join(map(str,ans[i])).replace('-1','#'))