a, b = (int(_) for _ in input().split())
if a == 1:
    a = 14
if b == 1:
    b = 14
print('Draw' if a == b else 'Alice' if a > b else 'Bob')