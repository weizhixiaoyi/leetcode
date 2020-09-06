# -*- coding:utf-8 -*-

def solve(nums):
    if not nums: return 0
    nums_len = len(nums)

    max_value = nums[0]
    cur_sum = nums[0]
    for i in range(1, nums_len):
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += nums[i]
        max_value = max(max_value, cur_sum)
    return max_value


if __name__ == '__main__':
    line = input().split(',')
    nums = list(map(int, line))
    ans = solve(nums)
    print(ans)
