n, r = (int(_) for _ in input().split())
if n < 10:
    print(r+100*(10-n))
else:
    print(r)