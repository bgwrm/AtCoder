a, v = (int(_) for _ in input().split())
b, w = (int(_) for _ in input().split())
t = int(input())
print('YES' if t*w <= t*v-abs(b-a) else 'NO')