# しゃくとり法
n = int(input())
a = [int(_) for _ in input().split()]
count, right = 0, 0
m = dict()
for left in range(n):
    while right < n and m.get(a[right], 0) == 0:
        m[a[right]] = m.get(a[right],0)+1
        right += 1
    count = max(count, right-left)
    m[a[left]] = m.get(a[left],1)-1
print(count)

# 動的計画法(DP)
n, w = 6, 8
weight = [2, 1, 3, 2, 1, 5]
value = [3, 2, 6, 1, 3, 85]
dp = [[0 for i in range(w+1)] for j in range(n+1)]
for i in range(n):
    for j in range(w+1):
        if j >= weight[i]:
            dp[i+1][j] = max(dp[i][j-weight[i]]+value[i],dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]
    print(dp[:i+2])
print(dp[n][w])

# Union-Find
class UnionFind(object):
    def __init__(self, n=1):
        self.par = [_ for _ in range(n)]
        self.rank = [0]*n
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
    def is_same(self, x, y):
        return self.find(x) == self.find(y)

n, m = 5, 3 #map(int, input().split()) n:ノードの数, m:パスの数
uf = UnionFind(n)
for i,j in [[1, 2],[5, 4],[4, 1]]:  # range(m):
    a, b = i, j #map(int, input().split()) #a,b:つながっている辺
    uf.union(a-1,b-1)
for i in range(n):
    uf.find(i)  # 一周findすることによって接続漏れをなくす。
print(uf.par) #[4, 4, 2, 4, 4]

# 周辺埋め
h, w = (int(_) for _ in input().split())
s = ["."*(w+2)]+["."+input()+"." for i in range(h)]+["."*(w+2)]
print(s)