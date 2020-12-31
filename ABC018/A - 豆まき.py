p = [int(input()) for _ in range(3)]
sorted_p = sorted(p, reverse=True)
for i in p:
    print(sorted_p.index(i)+1)