n = int(input())
a = [int(_) for _ in input().split()]
ans = 0

for i in a:
    ans += format(i, 'b')[::-1].find('1')

print(ans)