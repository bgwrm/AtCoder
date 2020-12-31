x = [int(_) for _ in input().split()]
l = [max(x)-x[0], max(x)-x[1], max(x)-x[2]]
print(sum(l)//2 if sum(l)%2 == 0 else (sum(l)+3)//2)