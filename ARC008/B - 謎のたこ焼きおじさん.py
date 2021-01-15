import math
n, m = (int(_) for _ in input().split())
name = input()
kit = input()
s = set(name)
ans = 0
for i in s:
    if i not in kit:
        print(-1)
        exit()
    ans = max(math.ceil(name.count(i)/kit.count(i)), ans)
print(ans)