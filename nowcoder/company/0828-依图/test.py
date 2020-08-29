# -*- coding:utf-8 -*-

from collections import defaultdict


def max_value(nums, nums_len):
    # print(nums)
    ans = 0
    left = 0
    for i in range(nums_len):
        while nums[i] != nums[left]:
            left = i

        ans = max(ans, i - left + 1)
    return ans


def solve(nums):
    nums_len = len(nums)

    # change k
    ans = max_value(nums, nums_len)
    for i in range(nums_len):
        if i == 0:
            cur_ans = max_value(nums[1] + nums[1:], nums_len)
        elif i == nums_len - 1:
            cur_ans = max_value(nums[0:-1] + nums[-1], nums_len)
        else:
            cur_ans = max_value(nums[0:i] + nums[i + 1] + nums[i + 1:], nums_len)
        ans = max(ans, cur_ans)
    return ans


if __name__ == '__main__':
    t = int(input())
    for k in range(t):
        line = input()
        ans = solve(line)
        print(str(ans))
