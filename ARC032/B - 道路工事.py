class UnionFind(object):
    def __init__(self, n = 1):
        self.par = [_ for _ in range(n)]
        self.rank = [0]*n
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
    def is_same_group(self, x, y):
        return self.find(x) == self.find(y)

n, m = (int(_) for _ in input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = (int(_) for _ in input().split())
    uf.unite(a-1, b-1)
for i in range(n):
    uf.find(i)
print(len(set(uf.par))-1)