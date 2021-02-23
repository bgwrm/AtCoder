n = int(input())
d = [int(input()) for _ in range(n)]
s, m = sum(d), max(d)
print(s)
print(max(2*m-s, 0))