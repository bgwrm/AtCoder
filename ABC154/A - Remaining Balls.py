s, t = (input().split())
a, b = (int(_) for _ in input().split())
u  = input()

if s == u:
    a -= 1
else:
    b -= 1

print(a, b)