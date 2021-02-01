n, l = 0, []

# bit全探索
# (i>>j)&1 iをjbitずらした数が1ならばTrue
for i in range(2**n):
    a = 0
    for j in range(n):
        if (i>>j)&1:
            a += l[j]

# 二分探索
import bisect
# 値aが挿入できる位置(同値があったときの左右)
left = bisect.bisect_left(l, a)
right = bisect.bisect_right(l, a)
# 挿入までする
bisect.insort_left(l, a)
bisect.insort_right(l,a)

# 深さ優先探索(DFS)

# 幅優先探索(BFS)

# 最短経路
ys, xs = 2, 2
yg, xg = 4, 5
a = ['########', '#......#', '#.######', '#..#...#', '#..##..#', '##.....#', '########']
n = [(ys-1, xs-1)]
route = {n[0]:0}
p = [[1, 0], [0, 1], [-1, 0], [0, -1]]
count = 1
while route.get((yg-1, xg-1), 0) == 0 and count != 10000:
    n2=[]
    for i in n:
        for j in p:
            np = (i[0]+j[0], i[1]+j[1])
            if a[np[0]][np[1]] == '.' and route.get(np, -1) == -1:
                n2.append(np)
                route[np] = count
    n = n2
    count += 1
print(n, route)

# ワーシャルフロイト法
import random
#from scipy.sparse.csgraph import floyd_warshall
c= [[random.randint(1, 10) for i in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] = min(c[i][j],c[i][k]+c[k][j])
for i in c:
    print(i)
cost=floyd_warshall(c)

# ベルマンフォード法
def BF(p, n, s):
    inf = float("inf")
    d = [inf for _ in range(n)]
    d[s-1] = 0
    for i in range(n+1):
        for e in p:
            if e[0] != inf and d[e[1]-1] > d[e[0]-1]+e[2]:
                d[e[1]-1] = d[e[0]-1] + e[2]
        if i == n-1:
            t = d[-1]
        if i == n and t != d[-1]:
            return [0,'inf']
    return list(map(lambda x:-x, d))
n, m = (int(_) for _ in input().split())
a = [[int(_) for _ in input().split()] for i in range(n)]
a = [[x,y,-z] for x,y,z in a]
print(BF(a, n, 1)[-1])

# ダイクストラ法
from heapq import heappop, heappush
mp2 = [[2, 4, 2], [3, 4, 5], [3, 2, 1], [1, 3, 2], [2, 0, 8], [0, 2, 8], [1, 2, 4], [0, 1, 3]]
inf = float('inf')
d = [inf for _ in range(5)]
d[0] = 0
prev = [None]*5
p, q = dict(), []
for i, j, k in mp2:
    p[i] = p.get(i,[])+[(j,k)]
print(p)
heappush(q,(d[0],0))
while q:
    print(q, d, prev)
    du, u = heappop(q)
    if d[u] < du:
        continue
    for v, weight in p.get(u,[]):
        alt = du+weight
        if d[v] > alt:
            d[v] = alt
            prev[v] = u
            heappush(q, (alt, v))
p=[4]
while prev[p[-1]] != None:
    p.append(prev[p[-1]])
print('最短経路',*p[::-1])
print('最短距離',d)