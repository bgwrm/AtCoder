n = int(input())
c = 1
while c*(c+1)//2 < n:
    c += 1
l = list(range(1,c+1))
if c*(c+1)//2 != n:
    l.remove(c*(c+1)//2-n)
print(*l, sep='\n')