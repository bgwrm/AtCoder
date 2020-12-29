n = int(input())
h = [int(_) for _ in input().split()]
ans = 0

while max(h) > 0:
    flg = True
    for i in range(len(h)):
        if h[i] > 0:
            h[i] -= 1
            flg = False
        elif h[i] == 0 and flg == False:
            break
    ans += 1

print(ans)