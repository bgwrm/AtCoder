n = int(input())
l = [list(input()) for _ in range(n)]
ans = [list(i) for i in zip(*l)]
for i in range(n):
    print(''.join(ans[i][::-1]))