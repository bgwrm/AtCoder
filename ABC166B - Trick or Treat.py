n, k = (int(_) for _ in input().split())
slist = []

for i in range(k):
    input()
    slist.extend(int(_) for _ in input().split())

print(n - len(set(slist)))