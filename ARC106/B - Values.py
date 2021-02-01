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

n, m = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
cd = [[int(_) for _ in input().split()] for i in range(m)]
uf = UnionFind(n)
sum_a = [0]*n
sum_b = [0]*n
for c, d in cd:
    uf.unite(c-1, d-1)
for i in range(n):
    r = uf.find(i)
    sum_a[r] += a[i]
    sum_b[r] += b[i]
print('Yes' if sum_a == sum_b else 'No')