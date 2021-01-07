s = input()
ss = set(s)
ans = 10**3
for st in ss:
    index = [i for i, x in enumerate(s) if x == st] + [len(s)]
    l = []
    for i in range(len(index)):
        if i == 0:
            l += [index[i]]
        else:
            l += [index[i]-index[i-1]-1]
    ans = min(max(l), ans)
print(ans)