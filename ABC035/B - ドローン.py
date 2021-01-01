s = input()
t = int(input())
now = [0,0]
q = 0

for i in s:
    if i == 'L':
        now[0] -= 1
    elif i == 'R':
        now[0] += 1
    elif i == 'U':
        now[1] += 1
    elif i == 'D':
        now[1] -= 1
    else:
        q += 1

d =abs(now[0])+abs(now[1])
if t == 1:
    print(d+q)
else:
    if d >= q:
        print(d-q)
    else:
        print((q-d)%2)