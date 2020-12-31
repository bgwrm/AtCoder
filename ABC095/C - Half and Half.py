a, b, c, x, y = (int(_) for _ in input().split())
ans = [max(x,y)*2*c, y*2*c+max(x-y,0)*a, x*2*c+max(y-x,0)*b, a*x+b*y]
print(min(ans))