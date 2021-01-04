abc = [int(_) for _ in input().split()]

if sum(i%2 == 0 for i in abc) > 0:
    print(0)
else:
    print(abc[0]*abc[1]*abc[2]//max(abc))