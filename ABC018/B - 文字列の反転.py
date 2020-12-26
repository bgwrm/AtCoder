s = ' ' + input()
n = int(input())

for i in range(n):
    l, r = (int(_) for _ in input().split())
    s = s[:l] + s[r:l-1:-1] + s[r+1:]

print(s[1:])