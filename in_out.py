# input/output
s = input()
n = int(input())
a, b = (int(_) for _ in input().split())
x = [int(_) for _ in input().split()]
l = [input() for _ in range(n)]
xy = [[int(_) for _ in input().split()] for i in range(n)]
x, y = [list(i) for i in zip(*xy)]
mod = 10**9 + 7
print('Yes' if n%2 == 0 else 'No')
print(*l, sep='\n')

# 組み合わせリスト
import itertools
com = list(itertools.combinations(l,2)) # nCr
per = list(itertools.permutations(l,3)) # nPr 順列
com = list(itertools.product(l, repeat=2)) # 重複可

# 出現数カウント
from collections import Counter
c = Counter(l)
print(c['s']) # sの出現回数
print(c.items()) # アイテム名と出現回数のタプル
print(c.most_common()) # 出現回数多い順

# アルファベットのリスト
print([chr(ord("a")+i) for i in range(26)])

# リスト読み込みと同時に添え字(_i)もつける
l = [(int(_), i) for i, _ in enumerate(input().split(), 1)]

# 優先度付きキュー
# 計算量O(logN)で最小値を取り出せる
# 最大値で使いたい場合は予め-1を掛けておく
import heapq
heapq.heapify(l) # リストを優先度付きキューに変換
heapq.heappop(l) # 最小値を取り出す
heapq.heappush(l, n) # 要素を挿入

# 複数indexを検索
li = [1,2,1,3,1]
indexes = [i for i, x in enumerate(list) if x == 1]
print(indexes) # [0, 2, 4]