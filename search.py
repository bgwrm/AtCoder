n, l = 0, []

# bit全探索
# (i>>j)&1 iをjbitずらした数が1ならばTrue
for i in range(2**n):
    a = 0
    for j in range(n):
        if (i>>j)&1:
            a += l[j]

# 二分探索
import bisect
# 値aが挿入できる位置(同値があったときの左右)
left = bisect.bisect_left(l, a)
right = bisect.bisect_right(l, a)
# 挿入までする
bisect.insort_left(l, a)
bisect.insort_right(l,a)