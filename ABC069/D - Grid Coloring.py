h, w = (int(_) for _ in input().split())
n = int(input())
a = [int(_) for _ in input().split()]
l = []
ans = [[0] * w for _ in range(h)]

for i in range(len(a)):
    l += [i + 1] * a[i]

count = 0
for i in range(h):
    for j in range(w):
        ans[i][j] = l[count]
        count += 1

for i in range(h):
    d = 1 if i % 2 == 0 else -1
    ans_i = ans[i][::d]
    print(' '.join(str(_) for _ in ans_i))