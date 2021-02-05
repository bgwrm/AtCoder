from collections import deque
n, m = (int(_) for _ in input().split())
p = [[] for _ in range(n)]
q = deque([0])
ans = [0]*(n)
for i in range(m):
    a, b = (int(_) for _ in input().split())
    p[a-1] += [b-1]
    p[b-1] += [a-1]
while q:
    now = q.popleft()
    for room in p[now]:
        if ans[room] == 0:
            ans[room] = now+1
            q.append(room)
print('Yes', *ans[1:], sep='\n')