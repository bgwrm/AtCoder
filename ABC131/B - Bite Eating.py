n, l = (int(_) for _ in input().split())
a = [l+i for i in range(n)]
print(sum(a)-min(a, key=abs))