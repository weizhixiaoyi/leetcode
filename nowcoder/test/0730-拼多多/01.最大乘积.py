# -*- coding:utf-8 -*-

# nums_len = 4
# nums = [-3, -4, 1, 2]
nums_len = int(input())
nums = list(map(int, input().split()))

max1, max2, max3 = 1, 1, 1
min1, min2 = 1, 1
# max1, max2, max3 = nums[0], nums[0], nums[0]
# min1, min2 = nums[0], nums[0]

for num in nums:
    if num >= max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num >= max2:
        max3 = max2
        max2 = num
    elif num >= max3:
        max3 = num

    if num <= min1:
        min2 = min1
        min1 = num
    elif num <= min2:
        min2 = num

print(max(min1 * min2 * max1, max1 * max2 * max3))
