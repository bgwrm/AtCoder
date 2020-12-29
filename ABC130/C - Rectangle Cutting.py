w, h, x, y = (int(_) for _ in input().split())
print(w*h/2, 1 if w == 2*x and h == 2*y else 0)