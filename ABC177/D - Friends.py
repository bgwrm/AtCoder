import networkx as nx
from networkx.utils.union_find import UnionFind
n, m = (int(_) for _ in input().split())
if m == 0:
    print(1)
    exit()
g = nx.Graph()
uf = UnionFind()
for i in range(m):
    a, b = (int(_) for _ in input().split())
    uf.union(a,b)
print(len(max(uf.to_sets(), key = len)))