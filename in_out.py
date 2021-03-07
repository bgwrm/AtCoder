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

# 小数点数扱うときはfloatじゃなくて
from decimal import Decimal
x, y, r = (Decimal(_) for _ in input().split())

# 組み合わせリスト
import itertools
com = list(itertools.combinations(l,2)) # nCr
per = list(itertools.permutations(l,3)) # nPr 順列
com = list(itertools.product(l, repeat=2)) # 重複可
com = list(itertools.combinations_with_replacement(l, 2)) #重複可順列

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

# キュー
# 先頭(終端)の要素に対する挿入・削除
from collections import deque
d = deque([l])
d.appendleft('element') # 先頭に要素を挿入
d.append('element') # 終端に要素を挿入
d.extendleft(['k', 'j']) # 先頭にリストを挿入
d.extend(['p', 'q']) # 終端にリストを挿入
d.popleft() # 先頭から要素を取り出す
d.pop() # 終端から要素を取り出す
d.rotate() # 右に要素をローテートさせる
d.rotate(-1) # 引数でいくつ動かすか指定できる(-1は左に1つ)

# 優先度付きキュー
# 計算量O(logN)で最小値を取り出せる
# 最大値で使いたい場合は予め-1を掛けておく
import heapq
heapq.heapify(l) # リストを優先度付きキューに変換
heapq.heappop(l) # 最小値を取り出す
heapq.heappush(l, n) # 要素を挿入

# 複数indexを検索
li = [1,2,1,3,1]
indexes = [i for i, x in enumerate(li) if x == 1]
print(indexes) # [0, 2, 4]

# 正規表現
import re
p = re.compile('[a-z]+')
s = 'abc'
if p.fullmatch(s):
    print('match')
else:
    print('no match')
# match