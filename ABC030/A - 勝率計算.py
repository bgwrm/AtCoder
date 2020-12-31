a, b, c, d = (int(_) for _ in input().split())
print('DRAW' if b*c == a*d else 'TAKAHASHI' if b/a > d/c else 'AOKI')