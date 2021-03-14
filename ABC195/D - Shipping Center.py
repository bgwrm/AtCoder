n, m, q = (int(_) for _ in input().split())
wv = sorted([[int(_) for _ in input().split()] for i in range(n)], key=lambda x: x[1], reverse=True)
x = [int(_) for _ in input().split()]
for _ in range(q):
    l, r = (int(_) for _ in input().split())
    box = sorted(x[:l-1]+x[r:])
    ni = [0]*len(box)
    for w, v in wv:
        for i in range(len(box)):
            if ni[i] == 0 and box[i] >= w:
                ni[i] = v
                break
    print(0 if len(ni) == 0 else sum(ni))