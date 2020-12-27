n = int(input())
a = [int(_) for _ in input().split()]
l = a[1::2][::-1] + a[0::2]
if len(a)%2 == 1:
    l = l[::-1]
print(' '.join(str(_) for _ in l))