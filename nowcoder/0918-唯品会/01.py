# -*- coding:utf-8 -*-


def solve(nums):
    nums_len = len(nums)
    # from collections import Counter
    # nums_count = Counter(nums)
    nums_count = {}
    for num in nums:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1
    for key, value in nums_count.items():
        if value >= nums_len // 2:
            return key


if __name__ == '__main__':
    nums = input().replace('[', '').replace(']', '')
    nums = nums.split(',')
    ans = solve(nums)
    print(ans)
