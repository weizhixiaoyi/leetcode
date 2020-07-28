# -*- coding:utf-8 -*-

while True:
    nums = list(map(int, input().split()))
    t = nums[0]
    if t == 0:
        break
    print(sum(nums[1:]))
    # print(((1 + t) * t) // 2)
