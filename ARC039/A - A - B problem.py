a, b = (input().split())
max_a = max(int('9'+a[1:]),int(a[0]+'9'+a[2]),int(a[:2]+'9'))
min_b = min(int('1'+b[1:]),int(b[0]+'0'+b[2]),int(b[:2]+'0'))
print(max(max_a-int(b),int(a)-min_b))