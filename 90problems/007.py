import bisect
n = int(input())
a = sorted([int(_) for _ in input().split()])
for _ in range(int(input())):
    b = int(input())
    i = bisect.bisect_left(a, b)
    if i == 0:
        print(a[0]-b)
    elif i == n:
        print(b-a[-1])
    else:
        print(min(a[i]-b, b-a[i-1]))