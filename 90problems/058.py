n, k = (int(_) for _ in input().split())
li, s = [n], 0
for i in range(10**9):
    tsugi = (sum(list(map(int, str(li[-1]))))+li[-1])%(10**5)
    if tsugi not in li: li += [tsugi]
    else: break
if k < len(li): print(li[k])
else:
    s = li.index(tsugi)
    print(li[s+(k-s)%(len(li)-s)])