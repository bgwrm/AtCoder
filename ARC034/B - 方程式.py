n = int(input())
c, l = 0, []
for i in range(max(1, n-9*(len(str(n)))), n+1):
    if i+sum(list(map(int, str(i)))) == n:
        c += 1
        l += [i]
print(c, *l, sep='\n')