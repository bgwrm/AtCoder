import heapq
n = int(input())
a = [int(_) for _ in input().split()]
mod = 10**9+7
heapq.heapify(a)
if n%2 and heapq.heappop(a) != 0:
    print(0)
    exit()
for _ in range(n//2):
    if heapq.heappop(a) != heapq.heappop(a):
        print(0)
        exit()
print(pow(2, n//2, mod))