n, m = (int(_) for _ in input().split())
a = [int(input()) for _ in range(m)][::-1] + list(range(1, n+1))
s = set()
for i in a:
    if i not in s:
        print(i)
        s.add(i)