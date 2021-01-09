h, w = (int(_) for _ in input().split())
print(0 if h==w==1 else w-1 if h==1 else h-1 if w==1 else w*(h-1)+h*(w-1))