x, y = (int(_) for _ in input().split())
ans = []
if -x == y:
    print(1)
    exit()
if x < y:
    ans += [y-x]
if -x < y:
    ans += [y+x+1]
if x < -y:
    ans += [-y-x+1]
if -x < -y:
    ans += [-y+x+2]
print(min(ans))