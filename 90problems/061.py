f, b, fc, bc = [], [], 0, 0
for _ in range(int(input())):
    t, x = (int(_) for _ in input().split())
    if t == 1:
        f += [x]
        fc += 1
    elif t == 2:
        b += [x]
        bc += 1
    else:
        if x > fc:
            print(b[x-fc-1])
        else:
            print(f[-x])