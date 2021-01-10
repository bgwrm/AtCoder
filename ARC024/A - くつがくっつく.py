l, r = (int(_) for _ in input().split())
li = [int(_) for _ in input().split()]
ri = [int(_) for _ in input().split()]
ans = 0
s = set(li+ri)
for i in s:
    ans += min(li.count(i), ri.count(i))
print(ans)