h, w = (int(_) for _ in input().split())
a = ''.join([input() for _ in range(h)])
print('Possible' if a.count('#')+1 == h+w else 'Impossible')