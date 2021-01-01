n, q = (int(_) for _ in input().split())
s = input()
li = [0] * n
c = 0

for i in range(1,n):
    if s[i-1:i+1] == 'AC':
        c += 1
    li[i] = c

for i in range(q):
    l, r = (int(_) for _ in input().split())
    print(li[r-1]-li[l-1])