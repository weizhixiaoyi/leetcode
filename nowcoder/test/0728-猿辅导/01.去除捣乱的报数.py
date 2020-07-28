# -*- coding:utf-8 -*-

nm = input().split()
n, m = int(nm[0]), int(nm[1])
nums = input().split()
nums = [int(v) for v in nums]

# n, m = 7, 2
# nums = [4, 3, 3, 3, 1, 5, 5]
# n, m = 6, 3
# nums = [1, 2, 2, 2, 2, 2]

from collections import defaultdict

nums_dict = defaultdict(int)
for num in nums:
    nums_dict[num] += 1

ans = []
for num in nums:
    if nums_dict[num] > m:
        continue
    ans.append(num)
ans = [str(v) for v in ans]

print(" ".join(ans))
