import heapq
n, m = (int(_) for _ in input().split())
a = [-1*int(_) for _ in input().split()]
heapq.heapify(a)
for i in range(m):
    p = heapq.heappop(a)
    heapq.heappush(a, -p//2*(-1))
print(-sum(a))