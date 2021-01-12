xy = [int(_) for _ in input().split()]
print(100000*(3*xy.count(1)+2*xy.count(2)+xy.count(3))+(400000 if xy.count(1) == 2 else 0))