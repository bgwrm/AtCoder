l = [int(_) for _ in input().split()]
for i in l:
    if l.count(i) == 1 or l.count(i) == 3:
        print(i)
        exit()