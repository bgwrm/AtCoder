import copy
def point(l):
    p = 0
    for i in range(9): p += (i+1)*10**l[i]
    return p
k, s, t = int(input()), list(input()), list(input())
sl, tl, c, w = [0]*9, [0]*9, [k]*9, 0
for i in range(4):
    c[int(s[i])-1] -= 1
    sl[int(s[i])-1] += 1
    c[int(t[i])-1] -= 1
    tl[int(t[i])-1] += 1
for i in range(1, 10):
    for j in range(1, 10):
        sln = copy.copy(sl)
        sln[i-1] += 1
        tln = copy.copy(tl)
        tln[j-1] += 1
        if point(sln) > point(tln):
            if i == j: w += c[i-1]*(c[j-1]-1)
            else: w += c[i-1]*c[j-1]
print(w/((9*k-8)*(9*k-9)))