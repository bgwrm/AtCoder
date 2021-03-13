import bisect
n = int(input())
l = [0]*(10**6+1)
for _ in range(n):
    l[int(input())] += 1
l = l[::-1]
for i in range(1, len(l)):
    l[i] += l[i-1]
q = int(input())
for _ in range(q):
    p = bisect.bisect_right(l, int(input()))
    print(10**6+1-p if p != 10**6 else 0)