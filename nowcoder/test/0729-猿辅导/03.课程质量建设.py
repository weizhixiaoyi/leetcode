# -*- coding:utf-8 -*-

# n, s = 6, 5
# nums = [5, 1, 1, 1, 2, 3]
ns = list(map(int, input().split()))
n, s = ns[0], ns[1]
nums = list(map(int, input().split()))

left = 0
cur_sum, ans = 0, 0

for i, num in enumerate(nums):
    cur_sum += num
    if cur_sum > s:
        ans = max(ans, i - left)
        cur_sum -= nums[left]
        left += 1

print(ans)
