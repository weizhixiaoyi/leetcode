# -*- coding:utf-8 -*-

nums_len = int(input())
nums = []
for i in range(nums_len):
    line = list(map(int, input().split()))
    nums.append(line)

# nums_len = 4
# nums = [
#     [1, 4],
#     [1, 2],
#     [2, 3],
#     [3, 4]
# ]

# nums_len = 3
# nums = [
#     [1, 6],
#     [2, 5],
#     [3, 4]
# ]

nums = sorted(nums, key=lambda d: d[1])

max_value = 0
for i in range(nums_len):
    center = nums[i]
    s, e = center[0], center[1]
    cur_value = 1
    for j in range(nums_len):
        if i == j: continue
        if nums[j][0] < s and nums[j][1] >= s:
            cur_value += 1
        elif nums[j][0] <= e and nums[j][1] > e:
            cur_value += 1
        elif nums[j][0] <= s and nums[j][1] >= e:
            cur_value += 1

    max_value = max(max_value, cur_value)
print(max_value)
