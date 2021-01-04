n = [int(_) for _ in input()]
print(max(sum(n), n[0]-1+9*(len(n)-1)))