# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

c = int(input())

for i in range(c):
    line = list(map(int, input().split()))
    t = line[0]

    import heapq

    nums = []
    for v in line[1: t + 1]:
        if v > 0: heapq.heappush(nums, -int(v))

    ans = 0
    while len(nums) >= 3:
        a = -heapq.heappop(nums)
        b = -heapq.heappop(nums)
        c = -heapq.heappop(nums)
        ans += 1

        a -= 1
        b -= 1
        c -= 1
        if a > 0: heapq.heappush(nums, -a)
        if b > 0: heapq.heappush(nums, -b)
        if c > 0: heapq.heappush(nums, -c)

    print(ans)
