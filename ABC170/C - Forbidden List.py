x, n = (int(_) for _ in input().split())
p = [int(_) for _ in input().split()]
diff = 0

if len(p) == 0:
    print(x)
    exit()

while True:
    if x - diff not in p:
        print(x - diff)
        exit()
    if x + diff not in p:
        print(x + diff)
        exit()
    diff += 1