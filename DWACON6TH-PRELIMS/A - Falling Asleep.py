n = int(input())
st = [input().split() for i in range(n)]
s, t = [list(i) for i in zip(*st)]
x = input()
print(sum(int(t[i]) for i in range(s.index(x)+1,n)))